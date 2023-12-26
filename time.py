hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

total_min = mins + dura
new_hour = (hour + total_min // 60) % 24
new_min = total_min % 60

print(str(new_hour)+':'+str(new_min))