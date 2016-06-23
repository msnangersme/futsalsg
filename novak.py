import requests
from pprint import pprint
from bs4 import BeautifulSoup
from time import time
from datetime import datetime

check_date = '2016-06-28'
check_time_start = '0900'
check_time_end = '1500'

print 'Kovansports.'
start_time = time()
s = requests.Session()

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
## offside
req_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length':29,
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': USER_AGENT,
    'Host': 'www.kovansports.com',
    'Origin': 'www.kovansports.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.kovansports.com/bookonline/',
    'Upgrade-Insecure-Requests': 1
}


req_data = {
    'date': datetime.strptime(check_date, '%Y-%m-%d').strftime("%d-%b-%y"),
    'load_schedule': 1
}

req_url = 'http://www.kovansports.com/bookonline/'

resp = s.post(req_url, data=req_data, headers=req_headers)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, 'html.parser')

timeslots = soup.findAll("input", {"class":"slotcheckbox"})

time_start = int(check_time_start)   #filter results based on start time- must be integer- without leading 0
time_end = int(check_time_end)     #filter results based on end time- must be integer- without leading 0
check_list = []
a=time_start
while a<time_end:
    check_list.append(a)
    a+=100

timeslots_dict = {}
for t in timeslots:
    pitch = int(t['value'][-1:])
    timeslot = int(t['value'][-6:-2])
    if timeslot>=time_start and timeslot<time_end:
        if pitch in timeslots_dict:
            timeslots_dict[pitch].append(timeslot)
        else:
            timeslots_dict[pitch] = [timeslot]

available=0
for pitch in timeslots_dict:
    if timeslots_dict[pitch] == check_list:
        print 'Pitch %s available.' %(pitch)
        available+=1
if available==0:
    print'No pitches available for selected date and time.'

print time()-start_time