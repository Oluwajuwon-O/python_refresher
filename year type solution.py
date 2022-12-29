year = int(input("Enter a year: "))

#
# Write your code here.
#	
if year >= 1582:
    if year % 4 != 0:
        print('Common year')
    elif year % 4 == 0:
        print('Leap year')
else:
    print('Not within the Gregorian calendar period')