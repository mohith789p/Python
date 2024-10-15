n = int(input('Enter the number of elements: '))
num = []
print('Enter the elements: ')
for i in range(n):
    num.append(int(input()))

print('Position of maximum: ', num.index(max(num)))
print('Position of minimum: ', num.index(min(num)))