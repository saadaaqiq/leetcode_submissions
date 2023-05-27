# https://leetcode.com/problems/kth-missing-positive-number

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k: 
            return k
        l, r = 0, len(arr)
        ml = 0
        while l < r:
            mid = (l+r)//2
            missing = arr[mid] - mid - 1
            if missing < k:
                ml = k - missing
                l = mid + 1
            else:
                r = mid
        return arr[l-1] + ml