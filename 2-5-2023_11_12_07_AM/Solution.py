# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, m: int) -> str:
        grid = [[] for i in range(m)]
        i = j = 0
        rev = False
        while j < len(s):
            grid[i].append(s[j])
            if i == 0 and i + 1 < m: 
                rev = False
                i += 1
            elif i == m-1 and m - 1 >= 0:
                rev = True
                i -= 1
            else:
                if not rev and i + 1 < m:
                    i += 1
                elif rev and i - 1 >= 0:
                    i -= 1
            j += 1
        return ''.join([''.join(c for c in r) for r in grid])