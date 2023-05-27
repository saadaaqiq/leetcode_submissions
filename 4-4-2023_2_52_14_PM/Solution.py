# https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        myset = set([chr(i + 97) for i in range(26)])
        res = 0
        for c in s:
            if c in myset:
                res += 1
                myset.clear()
            myset.add(c)
        return res
