import requests
from pprint import pprint
from bs4 import BeautifulSoup

if __name__ == '__main__':
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
        'date': '29-Jun-16',
        'load_schedule': 1
    }

    req_url = 'http://www.kovansports.com/bookonline/'

    resp = s.post(req_url, data=req_data, headers=req_headers)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, 'html.parser')

    timeslots = soup.findAll("input", {"class":"slotcheckbox"})


    time_start = 1800
    time_end = 2200
    print 'available slots-'
    for t in timeslots:
        pitch = int(t['value'][-1:])
        timeslot = int(t['value'][-6:-2])
        if timeslot>=time_start and timeslot<time_end:

            print 'kovansports pitch ' + t['value'][-1:] + ' ; time: '+ t['value'][-6:-2]
