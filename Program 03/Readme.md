# Program - 3:

> ## 1. Write a program to find the sum of first 10 natural numbers using i) for loop ii) while loop

## Code

```py
# using for loop
print("Using for loop:")
for i in range(1,11):
    print(i,end=" ")
print()

# using while loop
print("Using while loop:")
i=1
while(i<11):
    print(i,end=" ")
    i+=1
```

## Output

```text
Using for loop:
1 2 3 4 5 6 7 8 9 10
Using while loop:
1 2 3 4 5 6 7 8 9 10
```

> ## 2.Write a program to print multiplication table using i) for loop ii) while loop

## Code

```py
num = int(input('Enter a Number: '))
# using for loop
print("Using for loop:")
for i in range(1,11):
    print(num,'x',i,'=',num*i)

# using while
print("Using While loop:")
i = 1
while i<11:
    print(num,'x',i,'=',num*i)
    i+=1
```

## Output

```text
Enter a Number: 5
Using for loop:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Using While loop:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

> ## 3. Write a program to print each character of a string and string length

## Code

```py
word = input('Enterr a Sting: ')
print("length: ", len(word))
for i in word:
    print(i)
```

## Output

```text
Enterr a Sting: Python
length:  6
P
y
t
h
o
n
```

> ## 4. write a program to print factorial of a given number

## Code

```py
num = int(input('Enter a Number: '))
fact = 1
for i in range(num,0,-1):
    fact = fact * i
print('Factorial : ', fact)
```

## Output

```text
Enter a Number: 5
Factorial :  120
```

> ## 5. Write a program to check whether the given number is prime or not

## Code

```py
num = int(input('Enter a Number: '))
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count = count + 1
print('Prime : ', count == 2)
```

## Output

```text
Enter a Number: 97
Prime :  True
```

> ## 6. Write a program to check whether the given number is Armstrong or not

## Code

```py
num = int(input('Enter a Number: '))
temp = num
sum = 0
while num > 0:
    rem = num % 10
    num //= 10
    sum = sum + rem**3
print('Armstrong Number: ', sum == temp)
```

## Output

```text
Enter a Number: 153
Armstrong Number:  True
```

> ## 7. Write aid program to check whether the given number is Palindrome or not

## Code

```py
num = int(input('Enter a Number: '))
temp = num
sum = 0
while num > 0:
    rem = num % 10
    num //= 10
    sum = sum*10 + rem
print('Palindrome Number: ', sum == temp)
```

## Output

```text
Enter a Number: 53235
Palindrome Number:  True
```

> ## 8. Write a program to print the inverted left hand pyramid

## Code

```py
for i in range(5,0,-1):
    for j in range(i):
        print('* ',end = ' ')
    print()
```

## Output

```text
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
```

> ## 9. Write a program to find the sum of a series 1/1! + 2/2! + 3/3! + ...............+ n/n!.

## Code

```py
import math

n = int(input('Enter a Number: '))
total = 0
for i in range(1, n + 1):
    total += i / math.factorial(i)
print('Series Total: ', total)
```

## Output

```text
Enter a Number: 5
Series Total:  2.708333333333333
```

> ## 10. Write a program to print Floyd's triangle

## Code

```py
n = 1
for i in range(5):
    for j in range(i):
        print(n,end = ' ')
        n += 1
    print()
```

## Output

```text
1
2 3
4 5 6
7 8 9 10
```
