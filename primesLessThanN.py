import math

# Could do sieveOfEratosthene but have to look over. Off the top of my head
# was this solution
def isPrime(n):
    if n < 2:
        return False

    sqrtOfN = math.sqrt(n)
    for i in xrange(2,int(sqrtOfN)+1):
        if n % i == 0: 
            return False
    
    return True

def getNumberOfPrimes(n):
    primesLessThanN = [x for x in range(2, n) if x % 2 != 0]
    #print primesLessThanN
    #accounting for 2 base case
    primes = 1
    for i in range(len(primesLessThanN)):
        if isPrime(primesLessThanN[i]):
            #print primesLessThanN[i]
            primes = primes + 1
            
    return primes

print getNumberOfPrimes(int(raw_input()))