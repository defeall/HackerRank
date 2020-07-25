import calendar
import datetime 
c=input()
w=datetime.datetime.strptime(c, '%m %d %Y').weekday()
print(calendar.day_name[w].upper())
