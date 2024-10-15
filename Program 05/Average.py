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