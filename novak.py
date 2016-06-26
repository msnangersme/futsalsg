import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_kovansports_availability(check_date, check_time_start, check_time_end):
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
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
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

    for t in timeslots:
        pitch = int(t['value'][-1:])
        timeslot = int(t['value'][-6:-2])
        if timeslot in check_list:
            if pitch in available_pitches:
                available_pitches[pitch].append(timeslot)
            else:
                available_pitches[pitch] = [timeslot]

    for pitch in available_pitches:
        if available_pitches[pitch] == check_list:
            availability.append('Kovansports pitch %s' %(pitch))


    return availability

if __name__ == '__main__':
    check_date = '2016-06-28'
    check_time_start = '18:00'
    check_time_end = '20:00'

    print get_kovansports_availability(check_date, check_time_start, check_time_end)
