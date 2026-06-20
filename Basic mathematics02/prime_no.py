def checkPrime(n):
    count = 0 # Initialize a counter variable to count the number of factors
    for i in range(1,n+1):
        if n%i == 0:
            count+=1
    # If the number of factors is exactly 2 (1 and the number itself), it's prime
    return count == 2
n = 1483
isPrime = checkPrime(n)
if isPrime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")