import calendar, datetime

month, day, year = map(int, input().split())

# date = datetime.datetime(year,month,day)

# print(calendar.day_name[date.weekday()].upper())

date = calendar.weekday(year,month,day)

print(calendar.day_name[date].upper())