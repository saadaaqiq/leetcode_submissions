# https://leetcode.com/problems/sort-array-by-increasing-frequency

class Solution:
    def frequencySort(self, A: List[int]) -> List[int]:
        return chain(*([a]*b for a,b in sorted(list(Counter(A).items()), key=lambda x:(x[1],-x[0]))))