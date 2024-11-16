# Program - 5:

> ## 1. Write a program to find the sum and average of elements in a list.

## Code

```py
n = int(input('Enter the no. of elements: '))
num = []
sum = 0
print('Enter the elements: ')
for i in range(n):
    num.append(int(input()))
    sum += num[i]
avg = sum/n
print('Sum: ', sum)
print('Average: ', avg)
```

## Output

```text
Enter the no. of elements: 5
Enter the elements:
12
4
35
45
76
Sum:  172
Average:  34.4
```

> ## 2. Write a program to reverse a list.

## Code

```py
n = int(input('Enter the no. of elements: '))
lst = []
print('Enter the Elements: ')
for i in range(n):
    lst.append(int(input()))
# lst.reverse()
lst = lst[::-1]
print('Reversed List:')
print(lst)
```

## Output

```text
Enter the no. of elements: 5
Enter the Elements:
32
45
76
23
65
Reversed List:
[65, 23, 76, 45, 32]
```

> ## 3. Write a program to interchange the first and last elements in a list.

## Code

```py
n = int(input('Enter the no. of elements: '))
a = []
print('Enter the  elements: ')
for i in range(n):
    a.append(int(input()))
# a[0],a[n-1] = a[n-1],a[0]

swap =  a[0]
a[0] = a[n-1]
a[n-1] = swap

# a.insert(0,a.pop())
# a.append(a.pop(1))
print('After interchange first and last elements: ')
print(a)
```

## Output

```text
Enter the no. of elements: 5
Enter the  elements:
12
23
34
45
56
After interchange first and last elements:
[56, 23, 34, 45, 12]
```

> ## 4. Write a program to remove the first occurrence of an element in a list.

## Code

```py
n = int(input('Enter the no. of elements: '))
a = []
print('Enter the  elements: ')
for i in range(n):
    a.append(int(input()))
key = int(input('Enter the element you want to remove: '))
a.remove(key)
print(a)
```

## Output

```text
Enter the no. of elements: 7
Enter the  elements:
12
23
34
45
23
56
43
Enter the element you want to remove: 23
[12, 34, 45, 23, 56, 43]
```

> ## 5. Write a program to Extract Even and odd number from a given list in Python.

## Code

```py
n = int(input('Enter the number of elements: '))
num = []
print('Enter the elements: ')
for i in range(n):
    num.append(int(input()))
even, odd = [], []
for var in num:
    if var % 2 == 0:
        even.append(var)
    else:
        odd.append(var)
print('Even List:', even)
print('Odd List:', odd)
```

## Output

```text
Enter the number of elements: 8
Enter the elements:
12
23
34
45
56
67
78
89
Even List: [12, 34, 56, 78]
Odd List: [23, 45, 67, 89]
```

> ## 6. Write a program to find the positions of the minimum and maximum elements in a list.

## Code

```py
n = int(input('Enter the number of elements: '))
num = []
print('Enter the elements: ')
for i in range(n):
    num.append(int(input()))

print('Position of maximum: ', num.index(max(num)))
print('Position of minimum: ', num.index(min(num)))
```

## Output

```text
Enter the number of elements: 8
Enter the elements:
87
12
34
65
99
65
43
76
Position of maximum:  4
Position of minimum:  1
```

> ## 7. Write a program to find concatenate two lists index-wise.

## Code

```py
n = int(input('Enter the no. of elements: '))
lst1 = []
print('Enter the content in 1st list: ')
for i in range(n):
    lst1.append(input())

lst2 = []
print('Enter the content in 2nd list: ')
for i in range(n):
    lst2.append(input())

result = [''] * n
for i in range(n):
    result[i] = lst1[i] + lst2[i] # or append

print('After concatinating: ')
print(result)
```

## Output

```text
Enter the no. of elements: 4
Enter the content in 1st list:
M
na
i
Abhi
Enter the content in 2nd list:
y
me
s
Ram
After concatinating:
['My', 'name', 'is', 'AbhiRam']
```
