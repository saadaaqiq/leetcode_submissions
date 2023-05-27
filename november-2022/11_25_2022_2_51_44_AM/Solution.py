# https://leetcode.com/problems/sum-of-subarray-minimums

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        n = len(arr)
        tab = [-1]*n
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                tab[stack.pop()] = i
            stack.append(i)
        res = 0
        for i in range(n-1, -1, -1):
            if tab[i] == -1:
                tab[i] = (n-i)*arr[i]
            else:
                tab[i] = (tab[i]-i)*arr[i] + tab[tab[i]]
        return sum(tab) % (10**9 + 7)