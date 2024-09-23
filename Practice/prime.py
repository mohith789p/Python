# program to find all prime numbers in a given interval.

lowerInterval = int(input('Enter lower interval: '))
upperInterval = int(input('Enter upper interval: '))

# looping within the interval
for i in range(lowerInterval,upperInterval + 1):
    factors = 0
    j = 1
    while j <= i:
        if i % j == 0:
            factors += 1        # finding the factors
        j += 1
    if factors == 2:         # prime number has exactly two factors
        print(i)
