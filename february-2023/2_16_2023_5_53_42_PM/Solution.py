# https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = -math.inf
        q = deque()
        res = []

        for i, x in enumerate(nums):

            while q and x > q[-1][1]:
                q.pop()
            q.append((i, x))

            if i >= k-1:
                res.append(q[0][1])
            
            if i - q[0][0] >= k-1:
                q.popleft()
            
        return res
