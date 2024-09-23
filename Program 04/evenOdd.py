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
