n = int(input('Enter the no. of elements: '))
lst = []
print('Enter the Elements: ')
for i in range(n):
    lst.append(int(input()))
# lst.reverse()
lst = lst[::-1]
print('Reversed List:')
print(lst)