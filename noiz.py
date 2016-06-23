import urllib
from pprint import pprint
from bs4 import BeautifulSoup
import time

check_date = '2016-06-29'
check_time_start = '1900'
check_time_end = '2000'

start_time=time.time()
url = "http://www.zionsports.com.sg/booking/index.php?%s"

for pitch in (1, 2):
    params = urllib.urlencode({
        "option": "com_rsappt_pro2",
        "controller": "ajax",
        "task": "ajax_gad2",
        "format": "ajax",
        "gridstarttime": '%s:%s' %(check_time_start[:2], check_time_start[-2:] ),
        "gridendtime": '%s:%s' %(check_time_end[:2], check_time_end[-2:] ),
        "category": str(pitch),    #pitch number (1 or 2)
        "mode": "single_day",
        "resource": "0",
        "grid_date": check_date,
        "grid_days": "1",
        "gridwidth": "650px",
        "namewidth": "100px",
        "reg": "No",
        "browser":"Chrome",


    })
    # print url%params
    response = urllib.urlopen(url % params).read()
    soup = BeautifulSoup(response, 'html.parser')
    # pprint(soup.find_all("div"))
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
        counter=0

        for b in unavailable_dict:
            col= unavailable_dict[b]['left']
            start= unavailable_dict[b]['top']
            end= unavailable_dict[b]['top']+unavailable_dict[b]['height']

            if t_col == col and t_start>=start and t_start<=end:
                counter+=1
                availability_check+=1

        # if counter>0:
        #     print timeslots_dict[t]['timeslot'] + ': unavailable'
        # else:
        #     print timeslots_dict[t]['timeslot'] + ': available'
    if availability_check>0:
        print 'Pitch %s unavailable.' %(pitch)
    else:
        print 'Pitch %s available.' %(pitch)


print time.time()-start_time