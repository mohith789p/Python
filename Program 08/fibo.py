def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

terms = int(input("Enter the number of terms: "))
print("fibonacci Series:")
for i in range(terms):
    print(fibo(i), end=" ")