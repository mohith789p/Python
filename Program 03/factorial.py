num = int(input('Enter a Number: '))
fact = 1
for i in range(num,0,-1):
    fact = fact * i
print('Factorial : ', fact)