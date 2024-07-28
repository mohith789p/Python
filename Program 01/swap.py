# program to swap without using Tempary Variable

a = int(input('Enter a: '))
b = int(input('Enter b: '))

a = a + b       # storing total in a
b = a - b       # now subtracting b from total which gives a
a = a - b       # now subtracting b (which already became a) from total which gives b

print('after swapping:', a, b)
