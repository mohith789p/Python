# Program - 6:

> ## 1. Write a python program to reverse a given string.

## Code

```py
s = input("Enter a String: ")
print("Reversed String:",s[::-1])
```

## Output

```text
Enter a String: Mahesh
Reversed String: hsehaM
```

> ## 2. Write a python program to reverse a string without using the slicing operator.

## Code

```py
s = input("Enter the String: ")
rev = ""
for i in s:
	rev = i + rev
print("Reversed String: ",rev)
```

## Output

```text
Enter a String: Mahesh
Reversed String: hsehaM
```

> ## 3. Write a python program to check if a string is a palindrome.

## Code

```py
s=input("Enter the String: ")
if(s[::-1]==s):
	print(s,"is a palindrome")
else:
	print(s,"is not a palindrome")
```

## Output

```text
Enter the String: racecar
racecar is a palindrome
```

> ## 4.Write a python program to find the length of a string without using `len()` method.

## Code

```py
s = input("Enter a String: ")
c=0
for i in s:
	c+=1
print("Length: ",c)
```

## Output

```text
Enter a String: Python
Length:  6
```

> ## 5. Write a python program to count the number of vowels in a string.

## Code

```py
s = input("Enter a String: ")
vc = 0
for i in s:
	if i in "aeiouAEIOU":
		vc += 1
print("No. of Vowels: ", vc)
```

## Output

```text
Enter a String: Programming
No. of Vowels:  3
```

> ## 6. Write a python program to print even-length words in a string.

## Code

```py
s = input("Enter a String: ").split()
for i in s:
	if len(i) %2 == 0:
		print(i)
```

## Output

```text
Enter a String: i am laxmi
am
```
