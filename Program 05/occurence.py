n = int(input('Enter the no. of elements: '))
a = []
print('Enter the  elements: ')
for i in range(n):
    a.append(int(input()))
key = int(input('Enter the element you want to remove: '))
a.remove(key)
print(a)