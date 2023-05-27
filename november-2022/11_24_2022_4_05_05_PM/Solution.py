# https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A = nums1
        B = nums2
        if len(nums1) < len(nums2):
            B = nums1
            A = nums2
        m, n = len(A), len(B)
        half = (m+n)//2
        l, r = 0, n-1
        while True:
            b = (l+r)//2
            a = half - b - 2
            Bl = B[b] if b>=0 else -float("infinity")
            Br = B[b+1] if b+1<n else float("infinity")
            Al = A[a] if a>=0 else -float("infinity")
            Ar = A[a+1] if a+1<m else float("infinity")
            if Ar < Bl:
                r = b - 1
            elif Br < Al:
                l = b + 1
            else:
                return min(Ar, Br) if (m+n)%2 else (max(Al,Bl)+min(Ar,Br))/2    