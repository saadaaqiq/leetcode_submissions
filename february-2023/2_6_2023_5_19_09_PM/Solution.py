# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q, max_q = deque(), deque()
        i = 0
        for x in nums:
            while min_q and x < min_q[-1]:
                min_q.pop()
            while max_q and x > max_q[-1]:
                max_q.pop()
            min_q.append(x)
            max_q.append(x)
            if max_q and min_q and max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[i]:
                    max_q.popleft()
                if min_q[0] == nums[i]:
                    min_q.popleft()
                i += 1
        return len(nums) - i

                

            