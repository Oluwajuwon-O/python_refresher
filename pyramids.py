blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0

while height < blocks: # while the height is less than the blocks
    height += 1 # increase the height by 1
    blocks -= height # decrease the block by the current height
print("The height of the pyramid:", height)
