import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from classes import LinkFromHref
import random
import time
import pygame # for sound
from introscreen import logo
from os import system



target_url = "https://opensea.io/"
sample_header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# template for storing trending collections
featured = {
    'top_featured' : {'collection_name' : '', 'collection_link' : '', 'collection_desc' : ''},
    'rest_featured' : [{'name' : '', 'link' : '', 'desc': ''}]
}

# keep track of a previous listing until there's a change
previous_listing = {
    'topList' : [],
    'restList' : []
}
no_previous_listing = True

# timing (requests will be made every 4 - 6 min)
min_time = 0.5 * 60
max_time = 1.5 * 60
avg_wait_time = random.randint(min_time, max_time)

sound = None




def init():
    global sound
    pygame.init()
    pygame.mixer.init()
    sound_path = 'rsc/audio/Annoying_Alarm_Clock-UncleKornicob-420925725.wav'
    sound = pygame.mixer.Sound(sound_path)
    sound.set_volume(9/4)   # Now plays at 90% of full volume.



def raise_alarm(msg):
    print(msg)
    sound.play()



def fetch_data():
    global no_previous_listing

    # using requests
    s = requests.Session()
    s.headers.update(sample_header)
    request = s.get(target_url)

    # using Beautiful Soup
    url_prefix = "https://opensea.io"
    soup = BeautifulSoup(request.text, 'lxml')

   # print normal output.html
    with open("output/output.html", "w") as f:
        f.write(request.text)

    # find top featured collection
    top_card = soup.select('.Blockreact__Block-sc-1xf18x6-0.Flexreact__Flex-sc-1twd32i-0.elqhCm.jYqxGr.Featured--image-card')
    top_featured_a = f"{url_prefix}{top_card[0].a.get('href')}"
    top_collection_data = {'name' : '', 'link' : '', 'desc': ''} # empty dictionary
    top_collection_data = LinkFromHref(top_featured_a).get_collection_data()
    
    # =====================================================================================
    # DO NOT UNCOMMENT THESE UNLESS IT IS "DOOMSDAY PROTOCOL"
    # =====================================================================================
    # try:
    #     top_collection_data = LinkFromHref(top_featured_a).get_collection_data()
    # except:

    #     # write output to error.html
    #     with open("output/error.html", "w") as f:
    #         f.write(request.text)
        
    #     return
    # =====================================================================================
    # DO NOT UNCOMMENT THESE UNLESS IT IS "DOOMSDAY PROTOCOL"
    # =====================================================================================

    # update "featured" template
    featured['top_featured']['collection_name'] = top_collection_data['name']
    featured['top_featured']['collection_link'] = top_collection_data['link']
    featured['top_featured']['collection_desc'] = top_collection_data['desc']
    # print(featured['top_featured'])

    # find rest of the featured collections
    collections = soup.select('a.styles__StyledLink-sc-l6elh8-0.ekTmzq.PromoCard--main')
    # remove duplicates with set
    colls = list(set(collections))
    # print('no of collections: ', len(colls))
    for collection in colls:
        main_link = collection.get('href')
        featured_a = f"{url_prefix}{main_link}"
        collection_data = LinkFromHref(featured_a).get_other_collection_data()
        # print to template 
        featured['rest_featured'].append(
            {
                'name' : collection_data['name'],
                'link' : collection_data['link'],
                'desc': collection_data['desc']
            }
        )
    
    if no_previous_listing is True:
        # add to previous_listing
        # add featured['top_featured'] into a list in previous_listing['topList']
        previous_listing['topList'] = [featured['top_featured']]

        # add featured['rest_featured'] list as it is
        previous_listing['restList'] = featured['rest_featured']

        no_previous_listing = False
    
    # check for updates in the previous listing
    if no_previous_listing is False:
        
        # top featured
        if featured['top_featured'] != previous_listing['topList'][0]:
            msg = f"""
            ALERT
            =======================================================================
            [!] The top featured collection, {previous_listing['topList'][0]['collection_name']}, just got updated to {featured['top_featured']}
            =======================================================================
            \n\n"""
            raise_alarm(msg)
            no_previous_listing = True
        else:
            pass
        
        # rest featured
        previous_list = [i['name'] for i in previous_listing['restList']]
        new_list = [i['name'] for i in featured['rest_featured']]
        previous_set = set(previous_list)
        new_set = set(new_list)

        

        # 1, 2, 3, 4
        # 3, 2, 5, 6 (what has been removed => 1, 4) && (what has been added => 5, 6) in a set theory way
        # solution: difference of the set from previous to new only means "HE WHO REMAINS" (from Marvel's Loki)

        removed_collections = list(previous_set.difference(new_set))
        added_collections = list(new_set.difference(previous_set))
 

        removed = ''.join(removed_collections)
        added = ''.join(added_collections)
        
        if len(removed_collections) != 0 or  len(added_collections) != 0:
            msg = f"""
            ALERT
            ===============================================================
            [!] Removed Collections: {removed}
            ===============================================================
            [!] Newly listed Collections: {added}
            ===============================================================
            \n\n"""

            raise_alarm(msg)



def print_data():
    global featured
    # lastly
    # print top featured collection
    top = PrettyTable()
    top.field_names = ["Collection", "Link", "Description"]
    element = featured['top_featured']
    link = str(element['collection_link'])
    name = str(element['collection_name'])
    if name == "None":
        name = link.rsplit('/', 1)[-1]
    desc = str(element['collection_desc'][:75])
    top.add_row([name, link, desc])

    print('[+] Top featured collection')
    print('====================================')
    print(top)
    print("\n\n")

    # print other featured collections
    other = PrettyTable()
    other.field_names = ["Collection", "Link", "Description"]
    for element in featured['rest_featured']:
        link = str(element['link'])
        name = str(element['name'])
        if name == "None":
            name = link.rsplit('/', 1)[-1]
        desc = str(element['desc'][:75])
        other.add_row([name, link, desc])

    print('[+] Other trending, featured collections active right now')
    print('==========================================================')
    print(other)
    

    # save the data to a file

    import json
    from datetime import datetime
    
    
    with open('logs.txt', 'a') as fout:
        now = datetime.now()
        date = now.strftime("%a %d %b %H:%M:%S")
        time = now.strftime("%a %d %b %H:%M:%S")
        
        featured['date'] = date
        featured['time'] = time
        
        # Pretty Print JSON
        json_formatted_str = json.dumps(featured, indent=4, sort_keys=True)

        fout.write(json_formatted_str)
        fout.write("\n"*5)
    
    # empty featured
    
    featured = {
        'top_featured' : {'collection_name' : '', 'collection_link' : '', 'collection_desc' : ''},
        'rest_featured' : [{'name' : '', 'link' : '', 'desc': ''}]
    }



def main(intro):
    global avg_wait_time, min_time, max_time

    if intro is True:
        print(logo['normal'])

    while True:
        
        system('cls')
        print(logo['normal'])

        # fetch data
        fetch_data()

        #print data
        print_data()

        # delay
        avg_wait_time = random.randint(min_time, max_time)
        time.sleep(avg_wait_time)


init()
main(intro = True)
