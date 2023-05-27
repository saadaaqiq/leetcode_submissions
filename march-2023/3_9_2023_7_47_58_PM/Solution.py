# https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return sorted(list(count.keys()), reverse=True, key=lambda x:count[x])[:k]
