import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        #sieve of eratosthenes
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2, int(math.sqrt(n)) + 1 ):
            for j in range(i * i, n, i):
                isPrime[j] = False
        return sum(isPrime)