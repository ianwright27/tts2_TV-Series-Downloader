featured = {
    'top_featured': {'collection_name': 'HUEPHORIA', 'collection_link': 'https://opensea.io/collection/huephoria', 'collection_desc': 'Huephoria is a collection of 777 unique handcrafted Abstract digital artworks listed using a smart contract under ERC 721 token. Each artwork is authentic, hand drawn, unique and is accompanied by signature & frame surrounding the art which compliment the color spectrum of the artwork. Dimensions: 3000x3000px. https://www.drabstract.com/'}, 
    'rest_featured': [
        {'name': '', 'link': '', 'desc': ''}, {'name': None, 'link': 'https://opensea.io/collection/vandalz', 'desc': 'Vandalz for Ukraine: Wladimir Klitschko x WhIsBe is a historic collaboration with 100% of the proceeds going directly to Red Cross Ukraine, UNICEF Ukraine, and Ukrainian relief funds to support their vital efforts to provide humanitarian relief to the people of Ukraine.'}, {'name': 'Etherfauna', 'link': 'https://opensea.io/collection/rsconnett-etherfauna', 'desc': 'Original paintings and animations from LA based artist Robert S. Connett'}, {'name': 'M A N N E Q U I N S', 'link': 'https://opensea.io/collection/mannequins-by-reece-swanepoel', 'desc': 'M A N N E Q U I N S\nThis collection of 100 portraits is an almost academic attempt at reconciling order and chaos, universality and individuality, through expressive geometric art. Each piece is hand-painted, each with their own personality and purpose.\nThat\'s the idea behind my "mannequins". Each work is created from a stencil, but grows into its own individual character, just like we do.\nAnd ultimately, I just had fun with it! I hope you enjoy this selection too!'}, {'name': 'Singularity in Heritage by ORKHAN.ART', 'link': 'https://opensea.io/collection/singularityinheritage', 'desc': 'Singularity in Heritage, an AI-driven NFT exhibition at ArtDubai Digital Booth with GAZELL.iO, brings the innovation of Eastern visual arts, crafts, traditions, motifs and transmutes it to an experiment in cultural memory. Orkhan Mammadov aims to broaden the scope of a living tradition by bringing to life these new imagined rugs, coupled with data painting techniques, thread simulation, and color data. He opens up a space for a dialogue between the past and future, dystopia and utopia, to document and preserve the vast cultural history and tradition of the NFT future. As a result, Mammadov pushes the boundaries of tradition and digital and questions technology’s role as a form of memory and a tool of power.'}, {'name': None, 'link': 'https://opensea.io/collection/unf01d', 'desc': '-- 02 --'}, {'name': 'ARKIV by Alethea AI', 'link': 'https://opensea.io/collection/arkiv', 'desc': 'An ARKIV contains 11 unique AI-powered Assets.'}
    ]
}


from prettytable import PrettyTable

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
