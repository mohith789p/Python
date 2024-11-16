# Program - 8:

> ## 1. Write a program to find the factorial of a number using recursion.

## Code

```py
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

# Input from user
num = int(input("Enter a number: "))
print('Factorial: ',fact(num))
```

## Output

```text
Enter a number: 5
Factorial:  120
```

> ## 2. Write a program to print the Fibonacci sequence using recursion.

## Code

```py
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

terms = int(input("Enter the number of terms: "))
print("fibonacci Series:")
for i in range(terms):
    print(fibo(i), end=" ")
```

## Output

```text
Enter the number of terms: 5
fibonacci Series:
0 1 1 2 3
```

> ## 3. Write a program to find the GCD of two numbers using recursion.

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
enter first number:6
enter second number:9
gcd of (6, 9) is 3
```

> ## 4. Write a program to check if a given key exists in a dictionary.

## Code

```py
d = {1:'a',2:'b',3:'c',4:'d'}
key = int(input("Enter the key: "))
flag = 0
if key in d:
    print("Key is in dictionary")
    flag = 1
if flag == 0:
    print("Key is not found")
```

## Output

```text
Enter the key: 3
Key is in dictionary
```

> ## 5. Write a program to add a new key-value pair to an existing dictionary.

## Code

```py
d = {1:'a',2:'b',3:'c',4:'d'}
print("before: ",d)
d.update({5:'e'})
print("after: ",d)
```

## Output

```text
before:  {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
after:  {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
```

> ## 6. Write a program to sum all elements in a dictionary.

## Code

```py
d = {'a':1,'b':2,'c':3,'d':4}
sum = 0
for i in d.values():
    sum += i
print("Sum: ",sum)
```

## Output

```text
Sum:  10
```

> ## 7. Create a lambda function that returns "even" if a number is even, and "odd" if a number is odd.

## Code

```py
evenOdd = lambda num: "Even" if num % 2 == 0 else "Odd"
num = int(input("Enter a number: "))
print("Given number is", evenOdd(num))
```

## Output

```text
Enter a number: 25
Given number is Odd
```
