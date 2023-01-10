c0 = int(input("Enter c0: "))

if c0 > 1:
    # steps = 0
	# The while loop goes here.
    while c0 != 1:
        if c0 % 2 != 0:
			# Write your code here.
            cnew = 3 * c0 + 1
        else:
            cnew = c0 // 2
           
            print(cnew)
		# 
		# Write your code here.
		# 
# 	print("steps =",steps)
else:
	print("Bad c0 value")
