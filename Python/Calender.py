import calendar
import datetime
import time

print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))
print(calendar.weekheader(4))
print(calendar.weekheader(6))
print()

# index of first weekday i.e. monday is 0
print(calendar.firstweekday())

print(calendar.month(2021,3))
print(calendar.monthcalendar(2021,3))
print(calendar.calendar(2021))

week_day = calendar.weekday(2021,3,4)

print(week_day)

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days = calendar.leapdays(2020,2050)
print(how_many_leap_days)

