# Goal os repr is to be unambiguous
# Goal of str is to be readable

import datetime
import pytz

a = datetime.datetime.now(tz=pytz.timezone("Asia/Calcutta"))
b = str(a)

print(str(a))
print(str(b))

print()

print(repr(a))
print(repr(b))

# Output
# 2019-09-24 10:05:23.524441+05:30
# 2019-09-24 10:05:23.524441+05:30

# datetime.datetime(2019, 9, 24, 10, 5, 23, 524441, tzinfo=<DstTzInfo 'Asia/Calcutta' IST+5:30:00 STD>)
# '2019-09-24 10:05:23.524441+05:30'
