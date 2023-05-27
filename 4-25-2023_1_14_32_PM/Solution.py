# https://leetcode.com/problems/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(arr):
            if len(arr) <= 1: 
                return arr
            L, R = arr[:len(arr)//2], arr[len(arr)//2:]
            mergesort(L)
            mergesort(R)
            k, l, r = 0, 0, 0
            while l<len(L) and r<len(R): 
                (arr[k], l, r, k) = (L[l], l+1, r, k+1) if L[l] <= R[r] else (R[r], l, r+1, k+1)
            while l<len(L): 
                arr[k], l, k = L[l], l+1, k+1
            while r<len(R): 
                arr[k], r, k = R[r], r+1, k+1
            return arr                                
        
        return mergesort(nums)