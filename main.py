import os
import requests as r
from bs4 import BeautifulSoup as bs
import pyperclip
import time
import sys

#for debugging purposes
import webbrowser as wb
debug_url = 'http://www.stackoverflow.com/search?q=python+'
app_name = 'tts2.py'
logo = '''

		████████╗████████╗███████╗██████╗ 
		╚══██╔══╝╚══██╔══╝██╔════╝╚════██╗
		   ██║      ██║   ███████╗ █████╔╝
		   ██║      ██║   ╚════██║██╔═══╝ 
		   ██║      ██║   ███████║███████╗
		   ╚═╝      ╚═╝   ╚══════╝╚══════╝.py
		   	                     - Ian Wright
                                  
NOTE: Changing the Author's name doesn't make you the creator of the program
'''
instructions = '''
Today TV Series Downloader
=============================
For help use this commands
------------------------------
USAGE: %s <url> <path> <folder>

	> python %s -h             ---- For this help menu\n
	> python %s [url]          ---- To get download links from the movie's todaytvseries2 page
	> python %s [url] [path]   ---- Path to the directory where he files should be saved\n
	                                      eg "C:/Users/USER/Downloads/" , "/home/USER/Downloads" etc\n
	                                      NOTE: make sure the program is on path(beginners)... \n
	                                      or you can input the full path yourself (expert)
	                                      <--write it in quotation marks-->
	> python %s [url] [folder] ---- The folder you want to create
	                                <--write it in quotation marks-->

	Quick Example
	---------------
	> python %s https://www.example.com/movie.mp4 "C:/Users/user/Downloads" "Movies"\n

'''%( str(app_name),str(app_name),str(app_name), str(app_name), str(app_name), str(app_name))
links=[]
def clearScreen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def main():
	clearScreen()
	if len(sys.argv) == 2:
		argument1 = str(sys.argv[1])
		if argument1 == "-h":
			print(logo+instructions)
	elif len(sys.argv) > 2:
		#argument1 > url
		argument1 = str(sys.argv[1])
		argument2 = str(sys.argv[1]) #path
		argument3 = str(sys.argv[2]) #folder
		print(logo)
		print('[ * ] Fetching Links.... please wait')
		get_links(argument1,argument2, argument3)

	else:
		print(logo)
		print('\n[ * ] %s requires atleast one argument. Type "-h" for more information.'%(str(app_name)))

def download_file(link,cmd,folder):
	print('cmd => '+str(cmd))
	directory=''
	for char in cmd[1:-1]:
		if char == '/':
			char = '\\'
			directory += char
		else:
			directory+=char

	file_extension = link[len(link)-3:len(link)+1]
	file_name = link.split('/')[-1]
	new_dir = folder[1:-1]
	path = '%s\\%s'%(str(directory),str(new_dir))
	#check whether folder exists
	if os.path.exists(path) != True:
		print(path)
		os.system('md %s'%(path))

	file_path = '%s/%s'%(path, file_name)
	print('=> Downloading "%s" from Server'%(str(file_name)))

	_file_ = r.get(link, timeout=60, stream=True)
	bytedata = _file_.content
	with open(file_path, 'wb') as f:
		f.write(bytedata)
	print('\n\t => saved "%s" to "%s"'%(file_name, new_dir))

def list_files(arr, cmd,folder):
	clearScreen()
	print(logo+'\n')
	print('\n[ * ] Gonna download the following links:')
	for link in arr:
		print(str(link))
		download_file(link, cmd, folder)

def select_links(first, last, cmd,folder):
	download_list = links[first:last+1]
	list_files(download_list, cmd,folder)

def sort_links(cmd,folder):
	pos = 1
	print('Number \t Array \t Link\n')
	for i in range(0,len(links)):
		format_ = '%s). %s'%( str(pos),str(links[i]) )
		print(format_)
		pos+=1
	try:
		range_zero = raw_input('[ * ] Download from number: > ')
		range_last = raw_input('[ * ] To number > ')
	except:
		range_zero = input('[ * ] Download from number: > ')
		range_last = input('[ * ] To number > ')
	select_links(int(range_zero)-1, int(range_last)-1,cmd,folder)


def get_links(movie_url, cmd, folder):
	http = r.get(movie_url, timeout=60)
	page = bs(http.text, features='lxml')
	all_links_div = page.find_all('div', {'class':'cell4'})
	for div in all_links_div:
		link = div.find('a')
		links.append(link['href'])
	sort_links(cmd, folder)

try:
	main()
except Exception as e:
	print(e)
	wb.open(debug_url+str(e))
