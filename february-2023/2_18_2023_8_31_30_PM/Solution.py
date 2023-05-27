# https://leetcode.com/problems/sorting-the-sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        res = [''] * len(arr)
        for w in s.split():
            res[int(w[-1])-1] = w[:-1]
        return ' '.join(res)