# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        l1, l2 = len(a), len(b)
        res = [0] * (l2 + 1)
        ind = l2
        for i in range(l1 - 1, -1, -1):
            res[ind] += int(a[i])
            ind -= 1
        ind = l2
        c = 0
        for j in range(l2 - 1, -1, -1):
            t = c
            c = (res[ind] + int(b[j]) + c) // 2
            res[ind] = (res[ind] + int(b[j]) + t) % 2
            ind -= 1
        if c:
            res[0] = 1
        k = 0
        while k < l2 and res[k] == 0:
            k += 1
        return "".join([str(x) for x in res[k:]])
