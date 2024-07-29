n = int(input('Enter a Number: '))
sum = 0
for i in range(1,n+1):
    fact = 1
    for j in range (i,0,-1):
        fact *= j
    sum += i / fact
print('Series Total: ',sum)