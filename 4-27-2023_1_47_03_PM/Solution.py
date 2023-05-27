# https://leetcode.com/problems/sort-array-by-increasing-frequency

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return itertools.chain(*([num] * freq for (num,freq) in sorted(list(collections.Counter(nums).items()), key=lambda x:(x[1],-x[0]))))