# Program - 2:

> ## 1. Write a program to find the largest element among three numbers

## Code

```py
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
```

## Output

```text
Enter a: 70
Enter b: 86
Enter c: 45
86 is big.
```

> ## 2. write a program to check whether triangle is valid or not if sides are given

## Code

```py
a = int(input('Enter the First Side: '))
b= int(input('Enter the Second Side: '))
c = int(input('Enter the Third Side: '))

if a+b>c and b+c>a and c+a>b:
    print("Triangle is Valid")
else:
    print("Triangle is not Valid")
```

## Output

```text
Enter the First Side: 25
Enter the Second Side: 24
Enter the Third Side: 7
Triangle is Valid
```

> ## 3. Write a program to check whether given number is even or odd

## Code

```py
number = int(input('Enter a number: '))
if number%2 == 0:
    print(number,"is Even")
else:
    print(number,"is Odd")
```

## Output

```text
Enter a number: 69
69 is Odd
```

> ## 4. Write a program to check whether the given alphabet is vowel or consonant

## Code

```py
vowel = 'aeiouAEIOU'

letter = input('Enter a Alphabet: ')
if not letter.isalpha():
    print('INVALID!')
else:
    if letter in vowel:
        print(letter,"is Vowel")
    else:
        print(letter,"is Consonant")
```

## Output

```text
Enter a Alphabet: u
u is Vowel
```

> ## 5. Write a program to check whether the given year is Leap year or not

## Code

```py
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year,"is a leap year")

elif (year % 4 ==0) and (year % 100 != 0):
    print(year,"is a leap year")

else:
    print(year,"is not a leap year")
```

## Output

```text
Enter a year: 2024
2024 is a leap year
```

> ## 6. program to determine the grades based on marks
>
> | Grade |     Score      |
> | :---: | :------------: |
> |   A   |     >= 90      |
> |   B   | >= 80 and < 90 |
> |   C   | >= 70 and < 80 |
> |   D   | >= 60 and < 70 |
> |   E   | >= 50 and < 60 |
> | FAIL  |      < 50      |

## Code

```py
marks = float(input('Enter your marks: '))
if marks >= 90:
    print('GRADE: A')
elif marks >= 80:
    print('GRADE: B')
elif marks >= 70:
    print('GRADE: C')
elif marks >= 60:
    print('GRADE: D')
elif marks >= 50:
    print('GRADE: E')
else:
    print('FAILED')
```

## Output

```text
Enter your marks: 69
GRADE: D
```

> ## 7. write a program to determine the days of a week

## Code

```py
days=["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]
week = int(input("Enter the WEEK number(1-7): "))
index = week % 7
print("Days: ",days[index])
```

## Output

```text
Enter the WEEK number(1-7): 7
Days:  SUNDAY
```
