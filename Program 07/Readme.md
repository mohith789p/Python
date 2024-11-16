# Program - 7:

> ## 1. Write functions for basic arithmetic operations ( addition, subtraction, multiplication, division). Create a program that takes two numbers as input and return the result.

## Code

```py
def Arthimetic():
	print("addition: ",a+b)
	print("subtraction: ",a-b)
	print("multiplication: ",a*b)
	print("division: ",a/b)

a=int(input("enter a: "))
b=int(input("enter b: "))
Arthimetic()
```

## Output

```text
enter a: 5
enter b: 2
addition:  7
subtraction:  3
multiplication:  10
division:  2.5
```

> ## 2. Write a program to define a function with multiple return values.

## Code

```py
def calculate(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
rect_area, rect_perimeter = calculate(a, b)
print("Area of the rectangle: ", rect_area)
print("Perimeter of the rectangle: ", rect_perimeter)
```

## Output

```text
Enter first number: 15
Enter second number: 20
Area of the rectangle:  300
Perimeter of the rectangle:  70
```

> ## 3. Write a function to find the GCD of two numbers.

## Code

```py
def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)

a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("gcd of", (a,b),"is",gcd(a,b))
```

## Output

```text
enter first number:3
enter second number:9
gcd of (3, 9) is 3
```

> ## 4. Write a program to find the largest and smallest numbers in a list.

## Code

```py
def maxMin(l):
    return max(l),min(l)

n = int(input('Enter the no. of elements: '))
l = []
print('Enter the content in the list: ')
for i in range(n):
    l.append(input())
print("largest and smallest in ",l,"is",maxMin(l))
```

## Output

```text
Enter the no. of elements: 6
Enter the content in the list:
12
32
34
54
23
43
largest and smallest in  ['12', '32', '34', '54', '23', '43'] is ('54', '12')
```

> ## 5. Write a function to find the second-largest element in a list.

## Code

```py
def max(l):
    l.sort()
    print("the 2nd largest element in ",l,"is",l[-2])

n = int(input('Enter the no. of elements: '))
l = []
print('Enter the content in the list: ')
for i in range(n):
    l.append(input())
l=list(set(l))
max(l)
```

## Output

```text
Enter the no. of elements: 6
Enter the content in the list:
23
87
78
45
65
57
the 2nd largest element in  ['23', '45', '57', '65', '78', '87'] is 78
```

> ## 6. Write a function to flatten a list of lists into a single list.

## Code

```py
def flattenList(lst):
    flatList = []
    for items in lst:
        for item in items:
            flatList.append(item)
    return flatList

n = int(input("Enter the no. of lists: "))
l =[0] * n
for i in range(n):
    m = int(input(f"Enter the no. of elements in list {i+1} : "))
    print('Enter the elements in the list: ')
    l[i]= [input() for i in range(m)]
result = flattenList(l)
print("Flattened list: ", result)
```

## Output

```text
Enter the no. of lists: 2
Enter the no. of elements in list 1 : 5
Enter the elements in the list:
12
23
43
54
6
Enter the no. of elements in list 2 : 4
Enter the elements in the list:
12
32
4
3
Flattened list:  ['12', '23', '43', '54', '6', '12', '32', '4', '3']
```

> ## 7. Write a function to reverse a list without using built-in `reverse()` function or slicing.

## Code

```py
def list(l):
    n = len(l)
    for i in range(n//2):
        l[i],l[n-i-1] = l[n-i-1],l[i]
    return l

print(list([1,2,3,4]))
```

## Output

```text
[4, 3, 2, 1]
```
