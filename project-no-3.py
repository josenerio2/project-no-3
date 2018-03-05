import re
import os 
from datetime import datetime
from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
local_file = open('local_copy.log')

reg=re.compile(".*\[(.*) .*\] \".* (.*) .*\" (\d{3}) .*")

total_req=0
right=[]
parted=[]

mon=0
tue=0
wed=0
thur=0
fri=0
sat=0
sun=0

jan=0
feb=0
mar=0
apr=0
may=0
jun=0
jul=0
aug=0
sep=0
octo=0
nov=0
dec=0

un=0
suc=0

for line in local_file:
    for match in re.finditer(reg, line,):
        match_text = match.group()
        right.append(match_text)
        part = re.split(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*", line)
        if len(part)>=7:
            dt=datetime.strptime(part[1], "%d/%b/%Y")
            
            if dt.weekday==0:
                mon+=1
            elif dt.weekday==1:
                tue+=1
            elif dt.weekday==2:
                wed+=1
            elif dt.weekday==3:
                thur+=1
            elif dt.weekday==4:
                fri+=1
            elif dt.weekday==5:
                sat+=1
            elif dt.weekday==6:
                sun+=1
                
            if dt.month==1:
                jan+=1
            elif dt.month==2:
                feb+=1
            elif dt.month==3:
                mar+=1
            elif dt.month==4:
                apr+=1
            elif dt.month==5:
                may+=1
            elif dt.month==6:
                jun+=1
            elif dt.month==7:
                jul+=1
            elif dt.month==8:
                aug+=1
            elif dt.month==9:
                sep+=1
            elif dt.month==10:
                octo+=1
            elif dt.month==11:
                nov+=1
            elif dt.month==12:
                dec+=1
            

               
        total_req+=1
#print (un/total_req)
#print (suc/total_req)
print (total_req)            