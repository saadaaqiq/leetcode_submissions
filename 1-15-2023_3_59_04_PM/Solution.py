# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, H: List[int]) -> int:
        n = len(H)
        arr = [0] * n
        i, j = 0, n-1
        while i < j:
            area = abs(j-i) * min(H[i], H[j])
            arr[i] = max(arr[i], area)
            arr[j] = max(arr[j], area)
            if H[i] <= H[j]:
                i += 1
            elif H[i] > H[j]:
                j -= 1
        return max(arr)