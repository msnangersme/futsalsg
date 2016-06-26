import requests
from pprint import pprint


def get_offside_availability(check_date, check_time_start, check_time_end):
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

    req_url = 'http://offside.com.sg/wp-content/plugins/booking-system/frontend-ajax.php'

    for pitch in (1, 2):
        req_data = {
            'action': 'dopbs_load_schedule',
            'calendar_id': 1,
            'year': check_date[:4],
            'groundId': 1,
            'pitchId':pitch,
            'date':check_date
        }

        resp = s.post(req_url, data=req_data, headers=req_headers)
        resp.raise_for_status()
        results = resp.json()
        for hour in results[check_date]['hours']:
            if int(hour[:2]+hour[-2:]) in check_list:
                if results[check_date]['hours'][hour]['status']=='available':
                    if pitch in available_pitches:
                        available_pitches[pitch].append(int(hour[:2]+hour[-2:]))
                    else:
                        available_pitches[pitch] = [int(hour[:2]+hour[-2:])]

    for pitch in available_pitches:
        if sorted(available_pitches[pitch]) == check_list:
            availability.append('Offside pitch %s' %(pitch))

    return availability

if __name__ == '__main__':
    check_date = '2016-06-29'
    check_time_start = '17:00'
    check_time_end = '19:00'

    get_offside_availability(check_date, check_time_start, check_time_end)
