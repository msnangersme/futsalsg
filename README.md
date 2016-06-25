# test_repo

This script searches futsal facilities in Singapore for a given date and time and returns the available pitches.

    From terminal,
    1. cd to desired directory
    2. $git clone "https://github.com/aaronteoh/test_repo.git"
    3. $pip install bs4
    4. $python *desired directory*/test_repo/sportssearch.py YYYY-MM-DD HH:MM HH:MM

    selected date, start time (24hr clock), end time (24hr clock)
    if left empty, will check for next hour today

    For example, if installed in Documents folder, to search for next hour availability,
        $python /Users/intern/Documents/test_repo/sportsearch.py

    To search on 1 Jan 2017 from 5pm to 7pm,
        $python /Users/intern/Documents/test_repo/sportsearch.py 2016-01-01 17:00 19:00


Currently searches:
Bt Timah- The Cage
MacPherson- HYFA
Kallang- The Cage
Kovan- Kovan Sports Centre
Thomson- Offside
Zion Rd- Zion Sports Club
