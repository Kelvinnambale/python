hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# find a total of all minutes
mins = mins + dura
# find a number of hours hidden in minutes and update the hour
hour = hour + mins // 60
# correct minutes to fall in the (0..59) range
mins = mins % 60
# correct hours to fall in the (0..23) range
hour = hour % 24
print(hour, ":", mins, sep='')

print(1/1)

print(1 // 2 * 3)

x = int(input())
y = int(input())
 
x = x // y
y = y // x
 
print(y)
