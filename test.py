from datetime import datetime

check_date = '2016-06-28'
check_time_start = '0900'
check_time_end = '1500'

date = datetime.strptime(check_date, '%Y-%m-%d').strftime("%d-%b-%y")
time_start = '%s:%s' %(check_time_start[:2], check_time_start[-2:] )
time_end = '%s:%s' %(check_time_end[:2], check_time_end[-2:] )

print date
print time_start
print time_end

