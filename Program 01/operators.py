# program on using Operators

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print()

# Arthimetic Operators

print('Addition:', a + b)
print('Subtracion:', a - b)
print('Product:', a * b)
print('Division:', a / b)
print('Int Division:', a // b)
print('Modulus:', a % b)
print('Exponent:', a ** b)
print()

# Relational Operator

print("Equallity: ", a == b)
print("Greater than: ", a > b)
print("Less than: ", a < b)
print("Greater than or equal to: ", a >= b)
print("less than or equal to: ", a <= b)
print("Not Equallity: ", a != b)
print()

# bitwise operator

print('AND:', a & b)
print('OR:', a | b)
print('NOT FOR a:', ~a)
print('NOT FOR b:', ~b)
print('LEFT SHIFT FOR a: ', a << 1)
print('RIGHT SHIFT FOR a:', a >> 1)
print('LEFT SHIFT FOR b: ', b << 1)
print('RIGHT SHIFT FOR b:', b >> 1)
print()

#   Assignment Operator
c = a + b
print('Assigment: ', c)

# shorthand Assignment Operators
a += b
print("Addition Assignment: ", a)
a -= b
print("Subtraction Assignment: ", a)
a *= b
print("Multiplication Assignment: ", a)
a /= b
print("Division Assignment: ", a)
a //= b
print("Int Division Assignment: ", a)
a **= b
print("Exponent Assignment: ", a)
print()

# logical Operator

print('a,b are greater than 10:', a > 10 and b > 10)
print('a or b is greater than 10:', a > 10 or b > 10)
print('a,b are not greater than 10:', not (a > 10 and b > 10))
print()

# terinary oprator

max = a if a > b else b
print('Maximum:', max)
print()

# identity operator

print('a is b:', a is b)
print('a is not b:', a is not b)
print()

# membership operator
odd = [1,3,5,7,9]

print('5 is in odd:', 5 in odd)
print('8 is not in odd:', 8 not in odd)
