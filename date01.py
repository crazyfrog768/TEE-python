import datetime as dt

datenow = dt.datetime.now()
print(datenow)

date1 = dt.datetime(year=2022, month=2, day=14)
print(date1)

days = dt.timedelta(days=25)
date2 = date1 + days
print(date2)

print('------------------------------------')
date1 = dt.datetime(year=2022, month=2, day=14)
date2 = dt.datetime(year=2022, month=2, day=20)
days = date2- date1
print(days)

print('------------------------------------')
date1 = dt.datetime(
    year=2022, month=2, day=14,
    hour=13, minute=30
)

date2 = dt.datetime(
    year=2022, month=2, day=20,
    hour=16
)

days = date2 - date1
print(days)

print('------------------------------------')
print(date1.strftime('%A %d, %B %Y'))
