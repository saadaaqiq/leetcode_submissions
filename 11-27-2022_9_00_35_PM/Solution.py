# https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: 
            return 0
        primes = [False, False] + [True for i in range(n-2)]
        k = 2
        while k*k < n:
            if primes[k]:
                for i in range(k*k, n, k):
                    primes[i] = False
            k += 1
        return Counter(primes)[True]