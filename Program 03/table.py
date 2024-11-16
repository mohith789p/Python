num = int(input('Enter a Number: '))
# using for loop
print("Using for loop:")
for i in range(1,11):
    print(num,'x',i,'=',num*i)

# using while
print("Using While loop:")
i = 1
while i<11:
    print(num,'x',i,'=',num*i)
    i+=1