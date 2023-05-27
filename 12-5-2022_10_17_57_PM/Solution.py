# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr, A, B = s.split(" "), {}, {}
        if len(pattern) != len(arr): return False
        for i in range(len(arr)):
            if pattern[i] not in A: A[pattern[i]] = set()
            if arr[i] not in B: B[arr[i]] = set()
            A[pattern[i]].add(arr[i])
            B[arr[i]].add(pattern[i])
        for p in A:     
            if len(A[p])>1 or len(B[list(A[p])[0]])>1 or list(B[list(A[p])[0]])[0] != p: 
                return False
        return True

