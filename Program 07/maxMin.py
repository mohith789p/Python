def maxMin(l):
    return max(l),min(l)

n = int(input('Enter the no. of elements: '))
l = []
print('Enter the content in the list: ')
for i in range(n):
    l.append(input())
print("largest and smallest in ",l,"is",maxMin(l))