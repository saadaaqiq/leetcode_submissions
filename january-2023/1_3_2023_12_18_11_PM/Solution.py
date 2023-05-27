# https://leetcode.com/problems/delete-columns-to-make-sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for j in range(len(strs[0])):
            for i in range(len(strs)-1):
                if ord(strs[i][j]) > ord(strs[i+1][j]):
                    res += 1
                    break
                
        return res