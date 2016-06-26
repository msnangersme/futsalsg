import requests
from bs4 import BeautifulSoup
import re

def get_bttimahcage_availability(check_date, check_time_start, check_time_end):
    available_pitches={}
    availability = []

    check_list=[]
    a=int(check_time_start.translate(None, ':'))
    while a<int(check_time_end.translate(None, ':')):
        check_list.append(a)
        a+=100

    s = requests.Session()
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

    req_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'www.thecage.com.sg',
            'Pragma': 'no-cache',
            'Referer': 'http://www.thecage.com.sg/booking_bukittimah5/',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': USER_AGENT,


        }

    req_data = {
        'date' : check_date,
        'view' : 'week',
        'loc' : 'loc1'
    }

    req_url = 'http://www.thecage.com.sg/booking_bukittimah5/day_view.php'

    resp = s.get(req_url, params=req_data, headers=req_headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    timeslots = soup.findAll("a", href=re.compile('start_time='))

    for i in timeslots:
        params_raw = i['href'][len('/booking_bukittimah5/add_event.php?'):].split('&')
        params = dict(item.split('=', 1) for item in params_raw if '=' in item)

        if int(params['start_time'][:2]+params['start_time'][-2:]) in check_list:
            if i.text[-1:] in available_pitches:
                available_pitches[i.text[-1:]].append(int(params['start_time'][:2]+params['start_time'][-2:]))
            else:
                available_pitches[i.text[-1:]] = [int(params['start_time'][:2]+params['start_time'][-2:])]

    for pitch in available_pitches:
        if sorted(available_pitches[pitch]) == check_list:
            availability.append('Bt Timah cage pitch %s' %(pitch))

    return availability

if __name__ == '__main__':
    check_date = '2016-06-28'
    check_time_start = '19:00'
    check_time_end = '20:00'

    print get_bttimahcage_availability(check_date, check_time_start, check_time_end)
