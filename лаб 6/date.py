

# Write a Python program to subtract five days from current date.

from datetime import date, timedelta
dt= date.today()- timedelta(days=5)
print(dt)

# Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta
today= datetime.today()
yesterday= datetime.today() - timedelta(days=1)
tomorrow= datetime.today() + timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)

# Write a Python program to drop microseconds from datetime.
import datetime
dt=datetime.datetime.today().replace(microsecond=0)
print (dt)

# Write a Python program to calculate two date difference in seconds.

from datetime import date,datetime,timedelta
date1=date(2003,12,25)
date2=date(2023,10,29)
diff=date2-date1
print(diff.days*24*3600+ diff.seconds)
