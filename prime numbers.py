def is_prime(num):
#
# Write your code here.
#
    for i in range(2,num):
        if num % i == 0:
            return False
            break
    else:
        return True
    
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()


# num = 9

# for i in range(2,num):
#     if num % i == 0:
#         print(False)
#         break
# else:
#     print(True)
    
