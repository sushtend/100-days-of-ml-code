# https://www.youtube.com/watch?v=eirjjyP2qcQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=24
import datetime
import pytz

d = datetime.date(2019, 9, 23)  # only date and not time
tdy = datetime.date.today()
print(d)
print(tdy)

print(tdy.year)
print(tdy.weekday())  # Monday  = 0 Sunday = 6
print(tdy.isoweekday())  # Monday  = 1 Sunday = 7

# Time delta
tdelta = datetime.timedelta(days=7)
print(tdy + tdelta)

print(datetime.date(2019, 12, 23) - tdy)  # Returns delta if two dates are substratced

# ----------
dt = datetime.datetime(2019, 9, 23, 9, 12, 33, 1000)
print("Date time ", dt)
print("Extracting only date ", dt.date())

tdelta = datetime.timedelta(hours=6)
print("Adding Time Delta ", dt + tdelta)


# Timezone aware datetime
dt = datetime.datetime(2019, 9, 23, 9, 19, 33, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print("UTC Time : ", dt_utcnow)


# # To know all the timezones
# for tz in pytz.all_timezones:
#     print(tz)

dt_india = dt_utcnow.astimezone(pytz.timezone("Asia/Calcutta"))
print("India time: ", dt_india)

dt_india = datetime.datetime.now(tz=pytz.timezone("Asia/Calcutta"))
print(dt_india.strftime("%B %d, %Y"))

# strftime - converts datetime to string
# strptime - converts string to datetime

dt_str = "September 23, 2019"
dt_india = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt_india)
