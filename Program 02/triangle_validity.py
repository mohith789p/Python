a = int(input('Enter the First Side: '))
b= int(input('Enter the Second Side: '))
c = int(input('Enter the Third Side: '))

if a+b>c and b+c>a and c+a>b:
    print("Triangle is Valid")
else:
    print("Triangle is not Valid")
