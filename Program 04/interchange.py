n = int(input('Enter the no. of elements: '))
a = []
print('Enter the  elements: ')
for i in range(n):
    a.append(int(input()))
# a[0],a[n-1] = a[n-1],a[0]

swap =  a[0]
a[0] = a[n-1]
a[n-1] = swap

# a.insert(0,a.pop())
# a.append(a.pop(1))
print('After interchange first and last elements: ')
print(a)