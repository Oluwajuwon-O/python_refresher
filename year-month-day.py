def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if (year/4) % 2 == 0:
        return True
    else:
        return False
def days_in_month(year, month):
    month_31 = [1,3,5,7,10,12]
    month_30 = [4,6,9,11]
    if is_year_leap(year) == True:
        if month in month_31:
            return 31
        elif month == month_30:
            return 30
        else:
            return 29
    else:
        if month in month_31:
            return 31
        elif month in month_30:
            return 30
        else:
            return 28
#
# Write your new code here.
#

# print(is_year_leap(2000))
# print(days_in_month(2000, 2))
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
 	yr = test_years[i]
 	mo = test_months[i]
 	print(yr, mo, "->", end="")
 	result = days_in_month(yr, mo)
 	if result == test_results[i]:
         print("OK")
 	else:
         print("Failed")
