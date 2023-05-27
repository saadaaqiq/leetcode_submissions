# https://leetcode.com/problems/minimum-average-difference

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n, left, right, mini, min_ind = len(nums), [nums[0]], [0], float("infinity"), -1
        for i in range(1,n): left.append(left[-1]+nums[i])
        for i in range(n-1, 0, -1): right.append(right[-1]+nums[i])
        right = list(reversed(right))
        for i in range(n):
            left[i] = floor(left[i]/(i+1))
        for i in range(n-1):
            right[i] = floor(right[i]/(n-i-1))
        for i in range(n):
            absdiff = abs(left[i]-right[i])
            if absdiff < mini:
                mini = absdiff
                min_ind = i
        return min_ind
