#time ctime function => converts time expressed in seconds into local time
import time
print("ctime: ",time.ctime())

#time gmtime() converts time expressed in seconds to a struct time in UTC the dst is always zero
print("gmtime", time.gmtime())

#time localtime() method converts number of seconds into tlocal time
print ("localtime: ",time.asctime(time.localtime()))

#time mktime ()method inverse function of local time
t = (2024,10,14,10,5,45,0,288,0)
d = time.mktime(t)

print("mktime ", d)
print("asctime: ", time.asctime(time.localtime()))

#time sleep() execution for a given number or no seconds
print("Start: ", time.ctime())
time.sleep(5)
print("End: ", time.ctime())

#time strftime () method returns time to a specified argument
"""
Directive 
 %a - abbreviated weekday name 
 %A - full weekday name 
 %b - abbreviated month name 
 %B - full month name 
 %c - preferred date and time representation 
 %C - century number (the year divided by 100, range 00 to 99) 
 %d - day of the month (01 to 31) 
 %D - same as %m/%d/%y 
 %e - day of the month (1 to 31) 
 %g - like %G, but without the century 
 %G - 4-digit year corresponding to the ISO week number (see %V). 
 %h - same as %b 
 %H - hour, using a 24-hour clock (00 to 23) 
 %I - hour, using a 12-hour clock (01 to 12) 
 %j - day of the year (001 to 366) 
 %m - month (01 to 12) 
 %M - minute 
 %n - newline character 
 %p - either am or pm according to the given time value 
 %r - time in a.m. and p.m. notation 
 %R - time in 24 hour notation 
 %S - second 
 %t - tab character 
 %T - current time, equal to %H:%M:%S 
 %u - weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1 
 %U - week number of the current year, starting with the first Sunday as the first 
day of the first week 
 %V - The ISO 8601 week number of the current year (01 to 53), where week 1 is 
the first week that has at least 4 days in the current year, and with Monday as the 
first day of the week 
 %W - week number of the current year, starting with the first Monday as the first 
day of the first week 
 %w - day of the week as a decimal, Sunday=0 
 %x - preferred date representation without the time 
 %X - preferred time representation without the date 
 %y - year without a century (range 00 to 99) 
 %Y - year including the century 
 %Z or %z - time zone or name or abbreviation 
 %% - a literal % character """