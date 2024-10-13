import time
import calendar

ticks = time.time()

print("Number of ticks since 12am, january 1, 1970 is = ", ticks)


#time tuple
print(time.localtime())

#Getting current time
localtime = time.localtime(time.time())
print("Local current time is: ", localtime)

#Getting Formatted time
localtime=time.asctime(time.localtime(time.time()))
print("Local current time is: ", localtime)

#Getting calendar for a  month
cal = calendar.month(2024,1)
print("Here is the calendar: ")
print(cal)