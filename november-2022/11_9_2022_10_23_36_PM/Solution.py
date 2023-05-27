# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = 0
        res = 10000
        q = deque([(0, 0,nums[0])])
        while q: 
            ind, steps, possible_steps = q.popleft()
            if ind == len(nums)-1:
                res = min(res, steps)
            for i in range(possible_steps):
                if ind+i+1 > visited and ind+i+1 < len(nums):
                    q.append((ind+i+1, steps+1, nums[ind+i+1]))
                    visited = max(visited, ind+i+1)
        return res
