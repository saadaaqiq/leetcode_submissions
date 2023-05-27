# https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n1 = deque()
        n2 = []
        for n in nums:
            if n < 0:
                n1.appendleft(n*n)
            else:
                n2.append(n*n)
        res = []
        i, j = 0, 0
        while i < len(n1) or j < len(n2):
            if i == len(n1):
                res.append(n2[j])
                j += 1
            elif j == len(n2):
                res.append(n1[i])
                i += 1
            elif n1[i] <= n2[j]:
                res.append(n1[i])
                i += 1
            elif n1[i] > n2[j]:
                res.append(n2[j])
                j += 1
        return res

