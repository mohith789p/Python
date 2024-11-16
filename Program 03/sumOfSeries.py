import math

n = int(input('Enter a Number: '))
total = 0
for i in range(1, n + 1):
    total += i / math.factorial(i)
print('Series Total: ', total)