n = int(input('Enter the no. of elements: '))
lst1 = []
print('Enter the content in 1st list: ')
for i in range(n):
    lst1.append(input())

lst2 = []
print('Enter the content in 2nd list: ')
for i in range(n):
    lst2.append(input())

result = [''] * n
for i in range(n):
    result[i] = lst1[i] + lst2[i] # or append

print('After concatinating: ')
print(result)