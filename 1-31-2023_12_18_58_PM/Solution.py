# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] * n
        for i in range(n-1, -1, -1):
            j = i + 1
            while j < n:
                if nums[j] > nums[i]:
                    arr[i] = max(arr[i], 1 + arr[j])
                j += 1
        return max(arr)