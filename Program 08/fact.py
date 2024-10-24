def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

# Input from user
num = int(input("Enter a number: "))
print('Factorial: ',fact(num))