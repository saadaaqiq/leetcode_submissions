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
            if n == 1: 
                return arr[0]

            l_acc = 0
            ml = -math.inf
            max_left = [0] * n
            for i in range(n):
                l_acc += arr[i]
                ml = max(l_acc, ml)
                max_left[i] = ml

            r_acc = 0
            mr = -math.inf
            max_right = [0] * n
            for i in range(n-1, -1, -1):
                r_acc += arr[i]
                mr = max(r_acc, mr)
                max_right[i] = mr
                
            return max([max_right[i+1] + max_left[i] for i in range(n-1)])

        return max(circ(nums), sliding_window(nums))
