import os
import time
from colorama import Fore, Back, Style
import cv2
import pygame as pg
import requests
import tkinter

#checking online mode





#logo
def logo():
    print(Fore.GREEN + '''
    
    
    
 $$$$$$\                                                         $$$$$$$$\                  $$\           
$$  __$$\                                                        \__$$  __|                 $$ |          
$$ /  $$ |$$\   $$\  $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\           $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ 
$$$$$$$$ |$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ \____$$\          $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|
$$  __$$ |$$ |  $$ |$$ |  \__|$$ /  $$ |$$ |  \__|$$$$$$$ |         $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  
$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |     $$  __$$ |         $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ 
$$ |  $$ |\$$$$$$  |$$ |      \$$$$$$  |$$ |     \$$$$$$$ |         $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |
\__|  \__| \______/ \__|       \______/ \__|      \_______|         \__| \______/  \______/ \__|\_______/ 
                                                                                                          
                                                                                                          
                                                                                                          

    
    ''')


def check_online():
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    online = r.status_code
    if(online == 200):
        pass
    else:
        print(online)
        print("offline")
        exit()


def is_done():
    clear()
    print('''
    
    
    
$$$$$$$\                                
$$  __$$\                               
$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  
$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|
$$$$$$$  |\$$$$$$  |$$ |  $$ |\$$$$$$$\ 
\_______/  \______/ \__|  \__| \_______|
                                        
                                        
                                        

    
    
    ''')




def install_mysql():
    clear()
    logo()
    os.system('apt update && apt upgrade')
    os.system('apt install mysql-server')
    os.system('mysql_secure_installation')


def install_postgress():
    clear()
    logo()
    os.system('apt install postgresql postgresql-contrib')

def clear():
    os.system("clear")


def install_apache():
    clear()
    logo()
    os.system('apt update && upgrade')
    os.system('apt install -y httpd')
    os.system('apt install apache2')
    os.system('systemctl start httpd')
    is_done()

def install_nginx():
    clear()
    logo()
    os.system('apt update && upgrade')
    os.system('apt install nginx')
    os.system('ufw app list')
    os.system("ufw allow 'Nginx HTTP'")
    os.system('systemctl start nginx')
    os.system('systemctl enable nginx')
    os.system('systemctl reload nginx')
    is_done()

def setup_server():
    clear()
    logo()
    print('''

    Please select database type:

    -> [1] Apache
    -> [2] Nginx 
    -> [3] Back
    -> [4] Exit


    ''')

    choose_server_program = input()

    if choose_server_program == "1":
        install_apache()
    elif choose_server_program == "2":
        install_nginx()
    elif choose_server_program == "3":
        clear()
        lobby()
    elif choose_server_program == "4":
        clear()
        exit()
    else:
        setup_server()



def setup_db():

    print('''
    
    Please select one point:
    
    -> [1] MySQL
    -> [2] PostgressSQL
    -> [3] Back
    -> [4] Exit 
        
    ''')

    choose_db = input()
    if choose_db == "1":
        install_mysql()
    elif choose_db == "2":
        install_postgress()
    elif choose_db == "3":
        clear()
        logo()
        lobby()
    elif choose_db == "4":
        clear()
        logo()
        exit()
    else:
        setup_db()



#starting program




def lobby():
    print('''

        Please select one point:

        -> [1] Setup server 
        -> [2] Setup Database
        -> [3] Kill this server!
        -> [4] Exit 


    ''')

    choose = input()

    #choosing
    if choose == "1":
        setup_server()
    elif choose == "2":
        setup_db()
    elif choose == "3":
        format()
    elif choose == "4":
        exit()
    else:
        logo()
        lobby()




#start


def main():
    check_online()
    clear()
    logo()
    lobby()


#logic start
main()