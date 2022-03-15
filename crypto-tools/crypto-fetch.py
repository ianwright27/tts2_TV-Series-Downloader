import requests
import json
import time
import random
from playsound import playsound
from os import system
import pygame

pygame.init()
pygame.mixer.init()
sound_path = 'rsc/audio/crypto-alarm.wav'
sound = pygame.mixer.Sound(sound_path)
sound.set_volume(9/4)   # Now plays at 90% of full volume.


# useful variables
avg_wait_time = random.randint(60, 200) # whatever criteria you use
expected_value = 350000
intro_text = """


	 ██████  ██████  ██ ███    ██       ████████ ██████   █████   ██████ ██   ██ ███████ ██████  
	██      ██    ██ ██ ████   ██          ██    ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
	██      ██    ██ ██ ██ ██  ██ █████    ██    ██████  ███████ ██      █████   █████   ██████  
	██      ██    ██ ██ ██  ██ ██          ██    ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
	 ██████  ██████  ██ ██   ████          ██    ██   ██ ██   ██  ██████ ██   ██ ███████ ██   ██ 
	                                                                                             
	                                                                                             
	                                          Ian Wright                                         
	                                       ---------------                         
"""
output_methods = {
	"vlc" : {"command": "vlc /path/to/file/audio.wav --mmdevice-volume=1.25"},
	"playsound": {"command": "playsound('rsc/audio/crypto-alarm.wav')"}
}


# request header
header = {"accept": "application/json"}



# currency api
CURRENCY_API_KEY = "080769c31350aac71351"
currencies_url = f'https://free.currconv.com/api/v7/convert?q=USD_KES,KES_USD&compact=ultra&apiKey={CURRENCY_API_KEY}'

# crypto api
url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_market_cap=true&include_last_updated_at=true'



def get_eth_data(log):
	# ethereum value in USD
	eth = requests.get(url, header)
	eth_value = eth.json()['ethereum']['usd']

	# kenyan shillings equivalent of USD
	c = requests.get(currencies_url, header)
	kes_value = c.json()['USD_KES']

	# conversion to local currency
	value = float(eth_value * kes_value)
	final_value = "{:,.2f}".format(value)
	final_str = f"\t[+] Ethereum: KES {final_value}"

	if log is True:
		print(final_str)
	
	return value



def main(intro):
	if __name__ == "__main__":
	
		if intro is True:
			print(intro_text)
			print("\n\n")

		print(f"\t[!] Expected value: {expected_value}")
	
		while True:
			eth_price = 0
			price = 0

			time.sleep(avg_wait_time)
			
			try:
				eth_price = get_eth_data(log = True)
				print(f"\tstatus: {eth_price}")

			except TypeError:
				print('\t[*] Failed to retireve ethereum price. [Trying again]')			

			if (eth_price > expected_value):
				print("\t\t[!] You should now convert this asset to USDT")
				sound.play()


main(intro = True)
