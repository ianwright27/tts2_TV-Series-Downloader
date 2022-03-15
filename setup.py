from os import system
import time


dependencies_file = "requirements.txt"

print("[+] Welcome to Coin-Tracker setup...")
print("===================================================================")
time.sleep(2)

print("[+] Please wait as Coin-Tracker installs...")
print("===================================================================")
time.sleep(2)

# install dependencies
system(f"python -m pip install -r {dependencies_file}")

print("===================================================================")
print("[+] All required packages have been installed")
print('[+] To run, type "python crypto-fetch.py" in your favourite terminal app.')
print("[+] For help or more, check the README.md file or go to https://github.com/ianwright27/coin-tracker/blob/main/README.md")


