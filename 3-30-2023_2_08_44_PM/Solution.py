# https://leetcode.com/problems/reducing-dishes

class Solution:
    def maxSatisfaction(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        res = max(0, max([sum([arr[j] * (j-i+1) for j in range(i,n)]) for i in range(n-1, -1, -1)]))
        return res
        
            

        