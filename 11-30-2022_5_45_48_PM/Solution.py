# https://leetcode.com/problems/longest-subsequence-with-limited-sum

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        res = []
        for q in queries:
            l, r = 0, len(nums)
            while l < r:
                mid = (l+r)//2
                if nums[mid] < q:
                    l = mid + 1
                elif nums[mid] > q:
                    r = mid
                else:
                    break
            if nums[mid] <= q:
                res.append(mid + 1)
            else:
                res.append(mid)
        return res






