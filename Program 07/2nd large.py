def max(l):
    l.sort()
    print("the 2nd largest element in ",l,"is",l[-2])

n = int(input('Enter the no. of elements: '))
l = []
print('Enter the content in the list: ')
for i in range(n):
    l.append(input())
l=list(set(l))
max(l)