# https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        for num in nums:
            ndic = collections.defaultdict(int)
            for k in dic:
                ndic[k+num] += dic[k]
                ndic[k-num] += dic[k]
            dic = ndic
        return dic[target]
            

            
        