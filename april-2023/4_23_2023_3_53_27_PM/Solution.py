# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        dic = collections.defaultdict(set)
        for i, x in enumerate(time):
            dic[x % 60].add(i)
        for j, y in enumerate(time):
            res += len(dic[(60-y%60)%60]) - (1 if j in dic[(60-y%60)%60] else 0)
        return res // 2