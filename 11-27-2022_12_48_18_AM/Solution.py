# https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], t: int) -> int:
        n = len(nums)
        nums.sort()
        v = float("infinity")
        res = 0
        
        for j in range(n-2):
            i, k = j+1, n-1
            while i != k:
                x, y, z = nums[i], nums[j], nums[k]
                if abs(t-x-y-z) < v:
                    v = abs(t-x-y-z)
                    res = x + y + z
                if t - y < x + z:
                    k -= 1
                elif t - y > x + z:
                    i += 1
                else: 
                    return x+y+z
        return res


       




        
