# https://leetcode.com/problems/most-frequent-even-element

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        x, c = -1, 0
        for k,v in Counter(nums).items():
            if k % 2 == 0:
                if (v==c and x != -1 and k < x) or (v>c):
                    x = k 
                    c = v
        return x