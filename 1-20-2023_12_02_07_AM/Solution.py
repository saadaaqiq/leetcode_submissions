# https://leetcode.com/problems/longest-turbulent-subarray

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        tab = [arr[i+1] - arr[i] for i in range(n-1)]
        A = [(-((i+1)%2) + i%2)*tab[i] for i in range(n-1)]
        B = [(-(i%2) + (i+1)%2)*tab[i] for i in range(n-1)]

        print(A)
        print(B)
        
        def highest(nums):
            l = 0
            ml = 0
            for i in range(len(nums)):
                if nums[i] > 0:
                    l += 1
                    ml = max(ml, l)
                else:
                    l = 0
            return ml

        return max(highest(A)+1, highest(B)+1)



