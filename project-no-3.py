import re
import os.path
from datetime import datetime
from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
local_file = open('local_copy.log')

if not os.path.isfile(LOCAL_FILE):
    urllib.request.urlretrieve(logurl, "local_copy.log")
    print("Downloading file: \nFile saved to:".format(LOCAL_FILE))
    
fh=open(LOCAL_FILE)

total_req=0
right=[]
parted=[]
tfers=0
dead=0

months_req:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
days_req:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
mon_file = {1: "Jan.txt", 2: "Feb.txt", 3: "Mar.txt", 4: "Apr.txt", 5: "May.txt", 6: "Jun.txt", 7: "Jul.txt", 8: "Aug.txt", 9: "Sep.txt", 10: "Oct.txt", 11: "Nov.txt", 12: "Dec.txt"}

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
            
if not os.path.exists(mon_file[dt.month]):
    file = open(mon_file[dt.month]), "w")
    file.write(line)
    file.close
else:
    file = open(mon_file[dt.month]), "a")
    file.write(line)
    file.close
    
    
#print (un/total_req)
#print (suc/total_req)
print (total_req)            
