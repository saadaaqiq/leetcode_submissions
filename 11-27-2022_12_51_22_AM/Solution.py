# https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], t: int) -> int:
        n, res, v = len(nums), 0, float("infinity")
        nums.sort()
        for j in range(n-2):
            i, k = j+1, n-1
            while i != k:
                if abs(t - nums[i] - nums[j] - nums[k]) < v:
                    v, res = abs(t - nums[i] - nums[j] - nums[k]), nums[i] + nums[j] + nums[k]
                if t - nums[j] < nums[i] + nums[k]: k -= 1
                elif t - nums[j] > nums[i] + nums[k]: i += 1
                else: return nums[i] + nums[j] + nums[k]
        return res


       




        
