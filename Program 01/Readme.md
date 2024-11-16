# Program – 1:

> ## 1. Write a program to convert fahrenheit to Celsius

## Code

```py
fahrenheit = float(input('Enter temperature in Fahreheit: '))
celcius = (fahrenheit - 32) * 5 / 9 #converting fahrenheit to celcius
print('Temperature in Celcius: ', celcius)
```

## Output

```text
Enter temperature in Fahreheit: 128
Temperature in Celcius:  53.333333333333336
```

> ## 2. Write a program to slap two numbers without using temporary variable

## Code

```py
# program to swap without using Tempary Variable
a = int(input('Enter a: '))
b = int(input('Enter b: '))
a = a + b       # storing total in a
b = a - b       # now subtracting b from total which gives a
a = a - b       # now subtracting b (which already became a) from total which gives b
print('after swapping:', a, b)
```

## Output

```text
Enter a: 50
Enter b: 37
after swapping: 37 50
```

> ## 3. The write a program to find simple interest

## Code

```py
priniciple = float(input('Enter Priniciple Amount: '))
time = float(input('Enter Time Taken: '))
rate = float(input('Enter Rate of Interest: '))
interest = (priniciple*time*rate)/100
print('Simple Interest: ', interest)
```

## Output

```text
Enter Priniciple Amount: 2000
Enter Time Taken: 2.5
Enter Rate of Interest: 5
Simple Interest:  250.0
```

> ## 4. Write a program to find area and perimeter of rectangle

## Code

```py
length = float(input('Enter the length: '))
breadth = float(input('Enter the breadth: '))
perimeter = 2*(length + breadth)
area = length * breadth
print("Perimeter: ",perimeter)
print("Area: ",area)
```

## Output

```text
Enter the length: 25
Enter the breadth: 56
Perimeter:  162.0
Area:  1400.0
```

> ## 5. Write a program to find Area and Circumference of a circle

## Code

```py
PIE = 22/7
radius = float(input('Enter the radius: '))
circumference = 2*PIE*radius
area = PIE*(radius**2)
print("Circumference: ",circumference)
print("Area: ",area)
```

## Output

```text
Enter the radius: 7
Circumference:  44.0
Area:  154.0
```

> ## 6. write a program in python to input distance in kilometers time in minutes and find a speed

## Code

```py
distance = float(input('Enter the distance in kilometers: '))
time = float(input('Enter the time in minutes: '))
speed = distance/(time/60)
print('Speed: ',speed)
```

## Output

```text
Enter the distance in kilometers: 5
Enter the time in minutes: 3
Speed:  100.0
```

> ## 7. demonstrate the following operators in python with suitable examples i) Arithmetic operators ii) relational operators iii) assignment operators iv) logical operators v) bitwise operators vi) membership operators vii) identity operators

## Code

```py
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
```

## Output

```text
Enter a: 5
Enter b: 2

Addition: 7
Subtracion: 3
Product: 10
Division: 2.5
Int Division: 2
Modulus: 1
Exponent: 25

Equallity:  False
Greater than:  True
Less than:  False
Greater than or equal to:  True
less than or equal to:  False
Not Equallity:  True

AND: 0
OR: 7
NOT FOR a: -6
NOT FOR b: -3
LEFT SHIFT FOR a:  10
RIGHT SHIFT FOR a: 2
LEFT SHIFT FOR b:  4
RIGHT SHIFT FOR b: 1

Assigment:  7
Addition Assignment:  7
Subtraction Assignment:  5
Multiplication Assignment:  10
Division Assignment:  5.0
Int Division Assignment:  2.0
Exponent Assignment:  4.0

a,b are greater than 10: False
a or b is greater than 10: False
a,b are not greater than 10: True

Maximum: 4.0

a is b: False
a is not b: True

5 is in odd: True
8 is not in odd: True
```