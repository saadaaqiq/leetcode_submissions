# https://leetcode.com/problems/find-the-celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
    
        i = j = 0

        @cache
        def cached_know(a, b):
            return knows(a,b)

        while i < n and j < n:
            if i == j:
                j += 1
                continue
            if cached_know(i,j):
                i = j
            else:
                j += 1

        for k in range(n):
            if k != i and (not cached_know(k,i) or cached_know(i,k)):
                return -1

        return i
