from datetime import datetime, timedelta

import pytz

dt = datetime.now()
print(datetime.strftime(dt, "%d/%m/%Y %H:%M:%S"))
print(datetime.strftime(dt, "%d %b %y"))

dt_str = "11/16/2021 20:30:00"
dt2 = datetime.strptime(dt_str, "%m/%d/%Y %H:%M:%S")
print(dt2.year, dt2.month, dt2.day)

print(dt2.tzinfo)
tz = pytz.UTC
dt3 = dt2.replace(tzinfo=tz)
print(dt3)

tz2 = pytz.timezone("Europe/Istanbul")
dt4 = dt3.astimezone(tz2)
print(dt4)

dt5 = datetime(2021, 1, 1, 3, 0, 0)
dt6 = datetime(2021, 1, 1, 0, 0, 0)
dt7 = dt6 + timedelta(hours=3)
print(dt7 == dt5)

diff = dt5 - dt6
print(diff.total_seconds())