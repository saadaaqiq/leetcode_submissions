# https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1 + nums2)
        n = len(combined)
        if n % 2 == 1:
            return combined[n // 2]        
        return (combined[n // 2 - 1] + combined[n // 2]) / 2
