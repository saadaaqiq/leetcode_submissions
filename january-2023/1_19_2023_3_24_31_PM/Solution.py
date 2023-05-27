# https://leetcode.com/problems/subarray-sums-divisible-by-k

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        dic = { r : 0 for r in range(k) }
        s = 0
        for num in nums:
            s += num
            dic[s%k] += 1
        s = 0
        for num in nums:
            res += dic[s]
            s = (s+num)%k
            dic[s] -= 1
        return res
            
