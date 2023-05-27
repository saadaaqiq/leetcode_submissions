# https://leetcode.com/problems/find-the-celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
    
        candidate = 0

        @cache
        def cached_know(a, b):
            return knows(a,b)

        for i in range(n):
            if i == candidate:
                continue
            if cached_know(candidate, i):
                candidate = i
                        
        for k in range(n):
            if k == candidate:
                continue
            if knows(candidate, k) or not knows(k, candidate):
                return -1
                
        return candidate
