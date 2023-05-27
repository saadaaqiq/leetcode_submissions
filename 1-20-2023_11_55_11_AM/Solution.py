# https://leetcode.com/problems/check-distances-between-same-letters

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = { i: [] for i in range(26) }
        for j, c in enumerate(s):
            x = ord(c)-97
            if not d[x]:
                if c == len(s) - 1:
                    return False
                else:
                    d[x].append(j)
            else:
                if j - d[x][0] != distance[x] + 1:
                    return False
                else:
                    d[x].append(j)
        return True
