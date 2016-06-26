import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_hyfa_availability(check_date, check_time_start, check_time_end):
    available_pitches = {}
    availability = []

    check_list=[]
    a=int(check_time_start.translate(None, ':'))
    while a<int(check_time_end.translate(None, ':')):
        check_list.append(a)
        a+=100

    s = requests.Session()
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

    req_headers = {
            'Accept' : 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding' : 'gzip, deflate',
            'Accept-Language' : 'en-US,en;q=0.8',
            'Cache-Control' : 'no-cache',
            'Connection' : 'keep-alive',
            'Content-Length' : 39,
            'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host' : 'hyfa.com.sg',
            'Origin' : 'http://hyfa.com.sg',
            'Pragma' : 'no-cache',
            'Referer' : 'http://hyfa.com.sg/book-pitch/',
            'User-Agent' : USER_AGENT,
            'X-Requested-With' : 'XMLHttpRequest'
    }

    req_url = 'http://hyfa.com.sg/book-pitch/PitchSlots'

    for pitch in (3, 4, 5, 6, 7, 8, 9, 10):

        req_data = {
            'date' : datetime.strptime(check_date, '%Y-%m-%d').strftime("%d %B %Y, %A"), #29 June 2016, Wednesday',
            'pitchID' : pitch
        }

        resp = s.post(req_url, data=req_data, headers=req_headers)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.json()['slots'], 'html.parser')

        timeslots = soup.findAll("input")
        for timeslot in timeslots:
            if not timeslot.has_attr('disabled'):
                if int(timeslot['value'][:2]+timeslot['value'][3:5]) in check_list:
                    if pitch in available_pitches:
                        available_pitches[pitch].append(int(timeslot['value'][:2]+timeslot['value'][3:5]))
                    else:
                        available_pitches[pitch] = [int(timeslot['value'][:2]+timeslot['value'][3:5])]

    for pitch in available_pitches:
        if sorted(available_pitches[pitch]) == check_list:
            availability.append('HYFA pitch %s' %(pitch))

    return availability

if __name__ == '__main__':
    check_date = '2016-07-05'
    check_time_start = '18:00'
    check_time_end = '20:00'

    get_hyfa_availability(check_date, check_time_start, check_time_end)
