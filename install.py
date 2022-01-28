import time 
import os 

print("Start installing...")

install_setuptools = 'pip3 install setuptools==3.8.1'

install_colorama = 'pip3 install -r req.txt'

os.system(install_setuptools)
os.system(install_colorama)

print("Install - is Done")

print("Do you want start script now?(y/n)")
answer = input()

if answer == "y":
    start_script = 'python3 main.py'
    os.system(start_script)
else:
    print("Stoping....")