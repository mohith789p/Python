d = {1:'a',2:'b',3:'c',4:'d'}
key = int(input("Enter the key: "))
flag = 0
if key in d:
    print("Key is in dictionary")
    flag = 1
if flag == 0:
    print("Key is not found")