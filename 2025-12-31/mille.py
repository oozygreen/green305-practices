hour = 60 * 60 * 1000
print("hour : " + str(hour))

day = 24 * hour
print("day : " + str(day))

week = 7 * day
print("week : " + str(week))

year = 365 * day
print("year : " + str(year))

myage = 30 * year
print("myage : " + str(myage))

import datetime
now = datetime.datetime.now()
print("now : " + str(now))
print("year : " + str(now.year))
print("month : " + str(now.month))
print("day : " + str(now.day))
print("hour : " + str(now.hour))
print("minute : " + str(now.minute))
print("second : " + str(now.second))
print("microsecond : " + str(now.microsecond))
print("timestamp : " + str(now.timestamp()))
print("isoformat : " + str(now.isoformat()))
