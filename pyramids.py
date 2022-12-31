blocks = int(input("Enter the number of blocks: "))
height = blocks
step = 0
#
# Write your code here.
#	
while height > 0:
    height -= blocks
    blocks -= 1
    step += 1
    
print("The height of the pyramid:", step)
