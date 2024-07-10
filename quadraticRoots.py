import math
a = int(input('Enter the x2 co-efficient: '))
b = int(input('Enter the x co-efficient: '))
c = int(input('Enter the constant: '))

delta = b**2 - 4*a*c
if delta > 0:
    root1 = ( -b + math.sqrt(delta) )/ (2*a)
    root2 = ( -b - math.sqrt(delta) )/ (2*a)
    print('Roots are', root1, 'and', root2)
elif delta == 0:
    root1 = root2 = -b/ (2*a)
    print('Roots are equal and', root2)
else:
    print('Roots are Imaginary.')