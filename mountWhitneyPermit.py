#!/usr/bin/python

import requests
from pprint import pprint


# def get_offside_availability(check_date, check_time_start, check_time_end):
def get_offside_availability():
    # available_pitches={}
    # availability = []

    # check_list=[]
    # a=int(check_time_start.translate(None, ':'))
    # while a<int(check_time_end.translate(None, ':')):
    #     check_list.append(a)
    #     a+=100

    s = requests.Session()
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

    req_headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length':292,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': USER_AGENT,
        'Host': 'www.recreation.gov',
        'Origin': 'http://www.recreation.gov',
        # 'Pragma': 'no-cache',
        'Referer': 'http://www.recreation.gov/entranceDetails.do',
        # 'X-Requested-With': 'XMLHttpRequest'
        }

    req_url = 'http://www.recreation.gov/entranceDetails.do'

    # req_data = {
    #     'action': 'dopbs_load_schedule',
    #     'calendar_id': 1,
    #     'year': check_date[:4],
    #     'groundId': 1,
    #     'pitchId':pitch,
    #     'date':check_date
    # }

    req_data = {
        'permitTypeId': '1010581713',
        'entryDate': 'Sun Jul 31 2016',
        'pGroupSize': 1,
        'pLengthOfStay': '',
        'actionToken': 'BF3D583D-F297-430C-9AF7-6884D7AFDCB0',
        'searchRequired': 'true',
        'dateToday': '07/31/2016',
        'contractCode': 'NRS0',
        'parkId': '72201',
        'dateMinWindow': '07/31/2016',
        'dateMaxWindow': '07/31/2017'
    }

    resp = s.post(req_url, data=req_data, headers=req_headers)
    resp.raise_for_status()
    results = resp.text
    # for hour in results[check_date]['hours']:
    #     if int(hour[:2]+hour[-2:]) in check_list:
    #         if results[check_date]['hours'][hour]['status']=='available':
    #             if pitch in available_pitches:
    #                 available_pitches[pitch].append(int(hour[:2]+hour[-2:]))
    #             else:
    #                 available_pitches[pitch] = [int(hour[:2]+hour[-2:])]

    # for pitch in available_pitches:
    #     if sorted(available_pitches[pitch]) == check_list:
    #         availability.append('Offside pitch %s' %(pitch))

    print results

if __name__ == '__main__':
    # get_offside_availability(check_date, check_time_start, check_time_end)
    get_offside_availability()
