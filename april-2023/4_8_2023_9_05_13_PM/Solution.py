# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        return sorted(arr, key=lambda x:(Counter(format(x,"b"))["1"],x))