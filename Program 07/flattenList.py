def flattenList(lst):
    flatList = []
    for items in lst:
        for item in items:
            flatList.append(item)
    return flatList

n = int(input("Enter the no. of lists: "))
l =[0] * n
for i in range(n):
    m = int(input(f"Enter the no. of elements in list {i+1} : "))
    print('Enter the elements in the list: ')
    l[i]= [input() for i in range(m)]
result = flattenList(l)
print("Flattened list: ", result)
