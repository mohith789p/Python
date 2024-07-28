# Finding the largest of three Numbers

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

# checking if a is big
if a > b and a > c:
    print( a, "is big.")
# checking if b is big
elif b > a and b > c:
    print( b, "is big.")
# a and b are small then c is big
else:
    print( c, "is big.")
