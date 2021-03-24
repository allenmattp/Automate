import datetime, time


print(datetime.datetime.now())

dt = datetime.datetime(2021, 12, 31, 23, 59, 59)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

print(datetime.datetime.fromtimestamp(time.time()))

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))

dt = datetime.datetime.now()

year = datetime.timedelta(days=365)
print(dt + year)