# https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return A[0]
        if A[0] != A[1]: return A[0]
        if A[-1] != A[-2]: return A[-1]
        l, r = 0, n-1

        while l <= r:
            m = (l+r)//2
            if A[m] == A[m-1]:
                if (m-l)%2:
                    l = m+1
                else:
                    r = m-2
            elif A[m] == A[m+1]:
                if (m-l)%2:
                    r = m-1
                else:
                    l = m+2
            else:
                return A[m]
        return A[l]
