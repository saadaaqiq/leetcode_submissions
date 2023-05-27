# https://leetcode.com/problems/minimize-product-sum-of-two-arrays

class Solution:
    def minProductSum(self, A: List[int], B: List[int]) -> int:
        A.sort()
        B.sort(reverse=True)
        print(A)
        print(B)
        s = 0
        for i in range(len(A)):
            s += A[i] * B[i]
        return s