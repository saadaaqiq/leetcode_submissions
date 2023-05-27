# https://leetcode.com/problems/find-the-celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
    #   0   1   2   3   4   5
    
        i = j = 0

        while i < n and j < n:
            if i == j:
                j += 1
                continue
            if knows(j,i) and not knows(i,j):
                j += 1
            else:
                i = j
        print((i,j))
        for k in range(n):
            if k != i and (not knows(k,i) or knows(i,k)):
                return -1

        return i
