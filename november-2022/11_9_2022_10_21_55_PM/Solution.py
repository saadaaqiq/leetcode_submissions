# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_ind = 0
        res = 10000
        q = deque([(0, 0 ,nums[0])])
        while q: 
            ind, upto, steps = q.popleft()
            if ind == len(nums)-1:
                res = min(res, upto)
            for i in range(steps):
                if ind+i+1 > max_ind and ind+i+1 < len(nums):
                    q.append((ind+i+1, upto+1, nums[ind+i+1]))
                    max_ind = max(max_ind, ind+i+1)
        return res
