import datetime

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

def createDaysList(daysList, monthList):
    import time
    from datetime import date

    today = date.today()
    i = 0
    for y in range(today.year-1, today.year+1):
        for m in range(today.month, today.month+12):
            m = m%12
            if m == 0:
                m = 12
            firstday = datetime.date(y, m, 1)
            lastday = last_day_of_month(firstday)
            #print(firstday, ", ", lastday)
            daysList.append([firstday.strftime("%Y-%m-%d"), lastday.strftime("%Y-%m-%d")])
            monthList.append(firstday.strftime("%Y-%m"))


# main
daysList = []
monthList = []
createDaysList(daysList, monthList)
