from datetime import datetime, timedelta

def main():
    # task a
    cur_dateTime = datetime.now()
    basic_delta = cur_dateTime + timedelta(days = 365)
    print('basic timedelta of 365 days:', str(basic_delta))
    
    # task b
    print('Today is: ', cur_dateTime)
    
    # task c
    two_years_delta = cur_dateTime + timedelta(days = 730)
    print("Two years from now will be: ", str(two_years_delta))
    
    # task d
    multi_delta = cur_dateTime + timedelta(weeks=2, days=3)
    print ("In two weeks and 3 days it will be: ", str (multi_delta))
    
    # task e
    three_weeks_ago = cur_dateTime - timedelta(weeks=3)
    print ("Three weeks ago it was: ", three_weeks_ago.strftime("%A %B %d, %Y"))
    
    # task f
    christmas_this_year = datetime(cur_dateTime.year, 12, 25)

    if cur_dateTime > christmas_this_year:
        christmas_next_year = datetime(cur_dateTime.year + 1, 12, 25)
        days_left = (christmas_next_year - cur_dateTime).days
    else:
        days_left = (christmas_this_year - cur_dateTime).days

    print(days_left, " days left till next Christmas.")

        


if __name__ == '__main__':
    main()
