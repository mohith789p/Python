num = int(input('Enter a Number: '))
temp = num
sum = 0
while num > 0:
    rem = num % 10
    num //= 10
    sum = sum*10 + rem
print('Palindrome Number: ', sum == temp)