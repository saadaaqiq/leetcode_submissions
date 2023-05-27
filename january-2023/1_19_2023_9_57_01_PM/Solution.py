# https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def sliding_window(arr):
            n = len(arr)
            l = 0
            ml, mr = 0, 0
            cs, ms = 0, arr[0]
            for r in range(n):
                if cs < 0:
                    cs = 0
                    l = r
                cs += arr[r]
                if cs > ms:
                    ms = cs
                    ml, mr = l, r
            return ms
        
        def circ(arr):
            n = len(arr)
            if n == 1: return arr[0]
            L = [arr[0]] + [0] * (n-1)
            for i in range(1, n):
                L[i] = L[i-1] + arr[i]
            R = [0] * (n-1) + [arr[-1]]
            for i in range(n-2, -1, -1):
                R[i] = R[i+1] + arr[i]
            ML = [-math.inf for i in range(n)]
            ml = -math.inf
            for i in range(n):
                if L[i] > ml:
                    ml = L[i]
                ML[i] = ml
            MR = [-math.inf for i in range(n)]
            mr = -math.inf
            for i in range(n-1, -1, -1):
                if R[i] > mr:
                    mr = R[i]
                MR[i] = mr
            return max([ML[i] + MR[i+1] for i in range(n-1)])

        return max(circ(nums), sliding_window(nums))
