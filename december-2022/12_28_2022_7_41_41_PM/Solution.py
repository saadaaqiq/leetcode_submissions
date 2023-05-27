# https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        arr1, arr2 = [0]*(n+1), [0]*(n+1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s1[i] == s2[j]:
                    arr1[j] = 1 + arr2[j+1]
                else:
                    arr1[j] = max(arr1[j+1], arr2[j])
            for k in range(n):
                arr2[k] = arr1[k]
        return arr1[0]