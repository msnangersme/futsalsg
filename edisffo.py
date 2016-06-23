import requests
from pprint import pprint
import time
if __name__ == '__main__':
    start_time= time.time()
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
        'year': 2016,
        'groundId': 1,
        'pitchId':4,
        'date':'2016-06-22'
    }

    req_url = 'http://offside.com.sg/wp-content/plugins/booking-system/frontend-ajax.php'

    resp = s.post(req_url, data=req_data, headers=req_headers)
    resp.raise_for_status()

    pprint(resp.json())

    print time.time()-start_time