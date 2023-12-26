blocks = 1000
layer = 0

while blocks >= 0 :
    layer += 1
    blocks -= layer
    if blocks < 0:
        break
    print(blocks, layer)
print('the height is: ', layer-1)

