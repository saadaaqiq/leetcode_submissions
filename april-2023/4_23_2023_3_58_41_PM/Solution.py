# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = collections.defaultdict(list)
        for i, x in enumerate(time):
            dic[x % 60].append(i)
        return sum([len(dic[-y%60]) - bisect_right(dic[-y%60], j) for (j,y) in enumerate(time)])