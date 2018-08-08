# This script will block websites from being accessed by users during specific times of the day.
# This script is great for productivity
# Written by Pavon Dunbar using Python v3.7.0 on Aug 8, 2018


import time
from datetime import datetime as dt

# Call the system hosts file on Windows OS
hosts_temp='hosts'
hosts_path=r'C:\Windows\System32\drivers\etc\hosts'
redirect='127.0.0.1'

# List all websites to block including the www, non-www, and subdomain versions
block_website=['www.facebook.com','facebook.com','gmail.com','www.gmail.com','gmail.google.com','www.gmail.google.com']

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,16):
        print('Working Hours Began. Certain Websites Blocked.')
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in block_website:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")            
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in block_website):
                    file.write(line)
            file.truncate()
        print('Working Hours Ended. Websites Unblocked.')
    time.sleep(5)
