# https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = Counter(nums)
        j = 0
        for i in range(3):
            while i in c and c[i] > 0:
                nums[j] = i
                j += 1
                c[i] -= 1
        

