import requests
from pprint import pprint
import time

check_date = '2016-06-28'
check_time_start = '0900'
check_time_end = '1500'

start_time= time.time()

for pitch in (1, 2, 3, 4):
    s = requests.Session()

    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    ## offside
    req_headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Content-Length':87,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': USER_AGENT,
        'Host': 'offside.com.sg',
        'Origin': 'http://offside.com.sg',
        'Pragma': 'no-cache',
        'Referer': 'http://offside.com.sg/',
        'X-Requested-With': 'XMLHttpRequest'
    }

    req_data = {
        'action': 'dopbs_load_schedule',
        'calendar_id': 1,
        'year': check_date[:4],
        'groundId': 1,
        'pitchId':pitch,
        'date':check_date
    }

    req_url = 'http://offside.com.sg/wp-content/plugins/booking-system/frontend-ajax.php'

    resp = s.post(req_url, data=req_data, headers=req_headers)
    resp.raise_for_status()

    results = resp.json()

    check_list=[]
    a=int(check_time_start)
    while a<int(check_time_end):
        check_list.append(a)
        a+=100

    available_slots = []
    for hour in results[check_date]['hours']:
        if results[check_date]['hours'][hour]['status']=='available':
            if int(hour[:2]+hour[-2:]) in check_list:
                available_slots.append(int(hour[:2]+hour[-2:]))

    if sorted(available_slots) == check_list:
        print 'Pitch %s available.' %(pitch)
    else:
        print 'Pitch %s unavailable.' %(pitch)

print time.time()-start_time