import datetime
import calendar
for i in range(2019,2029):
    print(datetime.datetime(i,1,1).strftime("%w"))
    print(calendar.weekday(i,1,1)+1)