﻿my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list2 = []
#
# Write your code here.
#
for i in my_list:
    if i not in my_list2:
        my_list2.append(i)
my_list = my_list2[:]
print("The list with unique elements only:")
print(my_list)
