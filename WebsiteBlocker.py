import time
from datetime import datetime

host="hosts"   #have to change this to your own path usually at r"C:\Windows\System32\drivers\etc\hosts" and r for using "\"
redirect="127.0.0.1"  
websitelist=["netflix.com","www.netflix.com","youtube.com","www.youtube.com"] # the website to block


while(True):
    now=datetime.now()
    if datetime(now.year,now.month,now.day,8) < now < datetime(now.year,now.month,now.day,21,16):  #change time here 
        print("Work")
        with open(host,'r+') as file :
            content=file.read()
            for website in websitelist:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Not work time")
        with open(host,'r+') as file :
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websitelist):
                    file.write(line)
            file.truncate()
    time.sleep(3)

# change the file name of .py to .pyw to run in backgroung 