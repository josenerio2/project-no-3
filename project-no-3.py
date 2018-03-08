import re
import os.path
from datetime import datetime
from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'



if not os.path.isfile(LOCAL_FILE):
    urllib.request.urlretrieve(logurl, "local_copy.log")
    print("Downloading file: \nFile saved to:".format(LOCAL_FILE))

if not os.path.exists(LOCAL_FILE):
    print("Downloading file: ")
    urllib.request.urlretrieve(URL_PATH, "local_copy.log")
    

    
fh=open(LOCAL_FILE)

total_req=0
right=[]
parted=[]
tfers=0
dead=0
counter_months=0
counter=1

Jan=0
months_req=[0]*12
days_req={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for line in fh:        


for line in fh:
    for match in re.finditer(reg, line,):
        match_text = match.group()
        right.append(match_text)
        part = re.split(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*", line)
        if len(part)>=7:
            dt=datetime.strptime(part[1], "%d/%b/%Y")
            
            if int(part[6])>=300 and int(part[6])<=399:
                tfers+=1
            if int(part[6])>400 and int(part[6])<=499:
                dead+=1
               
            total_req+=1
#print (un/total_req)
#print (suc/total_req)
print (total_req)            

    part = re.split(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*", line)
    if len(part)>=7:
        dt=datetime.strptime(part[1], "%d/%b/%Y")
        
        #splits=part
        #months_req[dt.month]
        #if months_req[0]==1:
        #    months_req[0]+=1
        #days_req[dt.weekday()] += 1
        x=(part[1].split("/"))
        y=x[1]
        
        if y=='Jan':
            months_req[0]+=1
        elif y=='Feb':
            months_req[1]+=1
        elif y=='Mar':
            months_req[2]+=1
        elif y=='Apr':
            months_req[3]+=1
        elif y=='May':
            months_req[4]+=1
        elif y=='Jun':
            months_req[5]+=1
        elif y=='Jul':
            months_req[6]+=1
        elif y=='Aug':
            months_req[7]+=1
        elif y=='Sep':
            months_req[8]+=1
        elif y=='Oct':
            months_req[9]+=1
        elif y=='Nov':
            months_req[10]+=1
        elif y=='Dec':
            months_req[11]+=1
        
        days_req[dt.weekday()]+=1
        if int(part[6])>=300 and int(part[6])<=399:
            tfers+=1
        if int(part[6])>=400 and int(part[6])<=499:
            dead+=1
        #if x[1]=='Jan':
        #    months_req[0]+=1
        total_req+=1
        
       # print(y)
#print (total_req)            
#print (tfers)
#print (dead)
#print (days_req)

