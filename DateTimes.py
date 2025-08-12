import datetime

mytime = datetime.time(2,5,30) #it goes till mirosecond
mydate = datetime.date.today()
print(mytime.hour)
print(mydate)
print(mydate.day)
print(mydate.ctime())
mydate = datetime.date.today()
date2 = datetime.date(2019,11,8)
result = mydate - date2 #special type timedelta it is having its own set of attributes
print(result)
from datetime import datetime
mydatetime = datetime(2021,10,3,12,20,1) #we need to import it from the package else system feels we are calling the package itself which is not callable
print(mydatetime)
mydatetime=mydatetime.replace(year=2020)
print(mydatetime)
mydatetime2 = datetime(2021,10,3,0,20,1)
diff= mydatetime-mydatetime2
print(diff.seconds)