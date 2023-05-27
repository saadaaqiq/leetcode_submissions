# https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        v = float("infinity")
        res = 0
        
        for k in range(n-2):
            z = target - nums[k]
            i, j = k+1, n-1
            while i != j:
                s = nums[i] + nums[j]
                if abs(z - s) < v:
                    v = abs(z - s)
                    res = s + nums[k]
                if z < s:
                    j -= 1
                elif z > s:
                    i += 1
                else:
                    return target
        return res

