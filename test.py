from datetime import datetime, timedelta
from pytz import timezone

# check_date = '2016-06-28'
# check_time_start = '0900'
# check_time_end = '1500'
#
# date = datetime.strptime(check_date, '%Y-%m-%d').strftime("%d-%b-%y")
# time_start = '%s:%s' %(check_time_start[:2], check_time_start[-2:] )
# time_end = '%s:%s' %(check_time_end[:2], check_time_end[-2:] )
#
# print date
# print time_start
# print time_end

# start_time = datetime.now(timezone('Asia/Singapore')).replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
# end_time = datetime.now(timezone('Asia/Singapore')).replace(minute=0, second=0, microsecond=0) + timedelta(hours=2)
#
# print start_time.strftime("%Y-%m-%d")
# print start_time.strftime("%R")
#
# print end_time.strftime("%Y-%m-%d")
# print end_time.strftime("%R")
time = "01:00"

line = time.translate(None, ':')
print line