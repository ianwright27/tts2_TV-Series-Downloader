import os


log = []
lines = []

def clear_scrn():
    if 'nt' in os.name:
        os.system('cls')
    else:
        os.system('clear')

with open("requirements", "r") as f:
    lines = f.readlines()
    
print('[+] Downloading important files...')

for i in lines:
    clear_scrn()
    os.system(f'pip install {i}')
    logs.append(i)

for i in log:
    print(f'[+] Installed {i}')
print(f'[+] Setup finished....\n[+] Launch "python main.py" for more')
