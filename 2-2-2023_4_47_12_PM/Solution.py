# https://leetcode.com/problems/verifying-an-alien-dictionary

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = { c: ind for (ind, c) in enumerate(order) }

        for i in range(len(words)-1):
            j = 0
            while j < min(len(words[i]), len(words[i+1])):
                if dic[words[i][j]] < dic[words[i+1][j]]:
                    break
                elif dic[words[i][j]] > dic[words[i+1][j]]:
                    return False
                else:
                    j += 1
            if j > 0 and (j == len(words[i]) or j == len(words[i+1])):
                if len(words[i]) > len(words[i+1]):
                    return False
        return True