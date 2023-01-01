c = 16
step = 0
while c > 0:
    c //= 2
    step += 1
    if c < 1:   break
    print(c)
print('step:',step)