import requests
from bs4 import BeautifulSoup
from pprint import pprint

def get_zionsports_availability(check_date, check_time_start, check_time_end):

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
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'www.zionsports.com.sg',
        'Pragma': 'no-cache',
        'Referer': 'http://www.zionsports.com.sg/booking',
        'User-Agent': USER_AGENT

    }

    for pitch in (1,2):
        req_data = {
            'option': 'com_rsappt_pro2',
            'controller': 'ajax',
            'task': 'ajax_gad2',
            'format': 'raw',
            'gridstarttime': check_time_start,
            'gridendtime': check_time_end,
            'category': pitch,      #pitch num
            'mode': 'single_day',
            'resource': 0,
            'grid_date': check_date,
            'grid_days': 7,
            'gridwidth': '650px',
            'namewidth': '100px',
            'reg': 'No',
            'browser': 'Chrome'
        }

        req_url = "http://www.zionsports.com.sg/booking/index.php?%s"

        resp = s.get(req_url, params=req_data, headers=req_headers)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')

        timeslots = soup.findAll("div", {"class":"sv_gad_timeslot_available"})
        unavailable = soup.findAll("div", {"class": ["sv_gad_timeslot_booked","sv_gad_timeslot_book-off"]})

        a=0
        unavailable_dict = {}
        for i in unavailable:
            unavailable_dict[a]={
            i['style'].split('; ')[0].split(':')[0]: int(i['style'].split('; ')[0].split(':')[1][:-2]),
            i['style'].split('; ')[1].split(':')[0]: int(i['style'].split('; ')[1].split(':')[1][:-2]),
            i['style'].split('; ')[2].split(':')[0]: int(i['style'].split('; ')[2].split(':')[1][:-2]),
            i['style'].split('; ')[3].split(':')[0]: int(i['style'].split('; ')[3].split(':')[1][:-2])
            }
            a+=1

        b=0
        timeslots_dict = {}
        for i in timeslots:
            attribute = i['style'].split('; ')

            timeslots_dict[b]= {
                'timeslot': i['title'][11:],
                attribute[0].split(':')[0]: int(attribute[0].split(':')[1][:-2]),
                attribute[1].split(':')[0]: int(attribute[1].split(':')[1][:-2]),
                attribute[2].split(':')[0]: int(attribute[2].split(':')[1][:-2]),
                attribute[3].split(':')[0]: int(attribute[3].split(':')[1][:-2])
            }
            b+=1

        availability_check=0
        for t in timeslots_dict:
            t_col = timeslots_dict[t]['left']
            t_start = timeslots_dict[t]['top']

            for b in unavailable_dict:
                col= unavailable_dict[b]['left']
                start= unavailable_dict[b]['top']
                end= unavailable_dict[b]['top']+unavailable_dict[b]['height']

                if t_col == col and t_start>=start and t_start<=end:
                    availability_check+=1

        if availability_check==0:
            availability.append('Zionsports pitch %s' %(pitch))

    return availability


if __name__ == '__main__':
    check_date = '2016-06-28'
    check_time_start = '20:00'
    check_time_end = '21:00'

    print get_zionsports_availability(check_date, check_time_start, check_time_end)