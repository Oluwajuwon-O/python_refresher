
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
            break
    else:
        return True

for i in range(2, 100):
    if is_prime(i):
        print(i, end=" ")
