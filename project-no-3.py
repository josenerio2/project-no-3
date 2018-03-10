import re
import os.path
import collections
from datetime import datetime
import urllib.request

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.txt'
FILE_REQS="file_reqs.txt"

if not os.path.exists(LOCAL_FILE):
    print("Downloading file: ")
    urllib.request.urlretrieve(URL_PATH, "local_copy.txt")
#opens local file with parsed logs
fh=open(LOCAL_FILE)
fh_2=open(LOCAL_FILE)

#list that will print out the total files requested from parsed logs
req_amt=[]
#counter for total redirected requestes
tfers=0
#counter for total unsucessful requests
dead=0
#list that will count the total requests made each month
months_req=[0]*12
#will count the days of the week in which requests were made
days_req={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
#counter for total requests
total_req=0   

#takes opened local file and places total files requested in order of most requested to least requested
for line in fh_2:
    try:
        #splits log files into list that presents file types
        req_amt.append(line[line.index("GET")+4:line.index("HTTP")] )
    except:
        pass
counter=collections.Counter(req_amt)

print ("Downloading list of requested files from most requested to least requested:")
FILE_REQS=open("file_reqs.txt", "w")
for count in counter.most_common():    
    FILE_REQS.write(str(count[1])+" "+str(count[0]+"\n"))

fh_2.close()


#takes opened local file and splits log files into lists 
for line in fh:
    #splits parsed logs into elements seperated by a space
    part = re.split(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*", line)
    
    #checks to see which log files equaled to the regular expressions 
    if len(part)>=7:
        dt=datetime.strptime(part[1], "%d/%b/%Y")
        #splits list of regular expressions into a list of dates requested
        x=(part[1].split("/"))
        #takes the month from the split list
        y=x[1]
        total_req+=1
        #the series of if and elif statements will place the requested file according to its approporiate month
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
        
        #these if statements will check to see which requests were unsuccessful and which were transfers
        if int(part[6])>=300 and int(part[6])<=399:
            tfers+=1
        if int(part[6])>=400 and int(part[6])<=499:
            dead+=1
        

print("This is the total amount of requests made in the rime period represented in the log: ", total_req)

print ("There were ", months_req[0], "requests made on January")
print ("There were ", months_req[1], "requests made on February")
print ("There were ", months_req[2], "requests made on March")
print ("There were ", months_req[3], "requests made on April")
print ("There were ", months_req[4], "requests made on May")
print ("There were ", months_req[5], "requests made on June")
print ("There were ", months_req[6], "requests made on July")
print ("There were ", months_req[7], "requests made on August")
print ("There were ", months_req[8], "requests made on September")
print ("There were ", months_req[9], "requests made on October")
print ("There were ", months_req[10], "requests made on November")
print ("There were ", months_req[11], "requests made on December\n")
print ("The total amount of requests that were not successful is: ", dead,", which makes ", int((dead/total_req)*100), "%")
print ("The total amount of requests that were redirected elsewhere were: ", tfers, ", which makes ", int((tfers/total_req)*100), "%\n")
print ("The list of all files in order of most requested to least requested is in the 'file_reqs.txt' file")
