# https://leetcode.com/problems/sum-of-subarray-minimums

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, tab, n, res = [], [-1]*len(arr), len(arr), 0
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                tab[stack.pop()] = i
            stack.append(i)
        for i in range(n-1, -1, -1):
            tab[i] = (tab[i]-i)*arr[i] + tab[tab[i]] if tab[i] != -1 else (n-i)*arr[i]
        return sum(tab) % (10**9 + 7)