# https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, arr: List[int], k: int) -> List[int]:
        s = str(k)
        tab = [int(c) for c in s]
        if len(arr) < len(tab):
            arr, tab = tab, arr
        i, j = len(arr) - 1, len(tab) - 1
        c = 0
        while i >= 0:
            x = arr[i]
            y = tab[j] if j >= 0 else 0
            z = x + y + c
            arr[i] = z % 10
            c = z // 10
            j -= 1
            i -= 1
        return arr if c == 0 else [c] + arr