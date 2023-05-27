# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        enum = [(i,num) for (i,num) in enumerate(nums)]
        sub = enum[0:1]
        q = deque()
        q.append(sub)
        res = 0
        while q:
            s = q.popleft()
            maxi = -float("infinity")
            for i, num in s:
                if i==len(nums)-1:
                    return res
                if maxi < i + num:
                    maxi = i + num
            res += 1
            newsub = enum[len(s):maxi+1]
            q.append(newsub)
        