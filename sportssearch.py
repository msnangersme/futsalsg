from edisffo import get_offside_availability
from noiz import get_zionsports_availability
from novak import get_kovansports_availability
from egacgnallak import get_kallangcage_availability
from egachamittb import get_bttimahcage_availability
from afyh import get_hyfa_availability
from time import time
import multiprocessing as mp
from datetime import datetime, timedelta
from pytz import timezone
import sys

def print0(val):
    if val and len(val):
        for v in val:
            print("{0}".format(v))

if __name__ == '__main__':

    start=time()
    if len(sys.argv) == 1:
        start_time = datetime.now(timezone('Asia/Singapore')).replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
        end_time = datetime.now(timezone('Asia/Singapore')).replace(minute=0, second=0, microsecond=0) + timedelta(hours=2)
        check_date = start_time.strftime("%Y-%m-%d")
        check_time_start = start_time.strftime("%R")
        check_time_end = end_time.strftime("%R")

    else:
        check_date = sys.argv[1]
        check_time_start = sys.argv[2]
        check_time_end = sys.argv[3]

    concurrent_processes = mp.cpu_count()
    pool = mp.Pool(processes=concurrent_processes)

    [pool.apply_async(get_offside_availability, args=(check_date, check_time_start, check_time_end), callback=print0)    ,
    pool.apply_async(get_kovansports_availability, args=(check_date, check_time_start, check_time_end), callback=print0) ,
    pool.apply_async(get_zionsports_availability, args=(check_date, check_time_start, check_time_end), callback=print0)  ,
    pool.apply_async(get_kallangcage_availability, args=(check_date, check_time_start, check_time_end), callback=print0) ,
    pool.apply_async(get_bttimahcage_availability, args=(check_date, check_time_start, check_time_end), callback=print0) ,
    pool.apply_async(get_hyfa_availability, args=(check_date, check_time_start, check_time_end), callback=print0),
    ]
    pool.close()
    pool.join()

    print '%.2f sec.' %(time()-start)
