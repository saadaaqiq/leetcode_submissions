# https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordList: List[str]) -> List[str]:
        res = []
        cur = []
        wordSet = set(wordList)
        n = len(s)

        def backtrack(i):
            if i == n:
                if cur and ''.join(cur[-1]) in wordSet:
                    res.append(" ".join(["".join(word) for word in cur]))
            else:
                if not cur:
                    cur.append([])
                if cur[-1] and ''.join(cur[-1]) in wordSet:
                    cur.append([])
                    cur[-1].append(s[i])
                    backtrack(i+1)
                    cur[-1].pop()
                    cur.pop()
                cur[-1].append(s[i])
                backtrack(i+1)
                cur[-1].pop()

        backtrack(0)

        return res