# https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        somme = 0
        res = 0
        for num in nums:
            somme += num
            if somme - k in prefixSums:
                res += prefixSums[somme-k]
            if somme not in prefixSums:
                prefixSums[somme] = 0
            prefixSums[somme] += 1
            
        return res

