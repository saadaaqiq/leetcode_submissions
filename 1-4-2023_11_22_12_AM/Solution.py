# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        res = 0
        for x in Counter(tasks).values():
            if x == 1: return -1
            res += x//3 + (1 if x%3 else 0)
        return res