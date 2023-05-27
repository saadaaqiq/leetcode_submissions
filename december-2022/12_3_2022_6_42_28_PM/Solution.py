# https://leetcode.com/problems/get-maximum-in-generated-array

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0 or n==1: return n
        arr = [0, 1]
        for i in range(2, n+1):
            arr.append(arr[i//2] + (arr[(i+1)//2] if i%2 != 0 else 0))
        return max(arr)