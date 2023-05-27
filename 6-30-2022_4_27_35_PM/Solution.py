# https://leetcode.com/problems/valid-parenthesis-string

class Solution:
  def checkValidString(self, s: str) -> bool:
    temp = set([0])
    for c in s:
      temp = temp.union(set([k+1 for k in temp if k+1 >= 0])).union(set([k-1 for k in temp if k-1 >= 0])) if c == '*' \
        else (set([k+1 for k in temp if k+1 >= 0]) if c == '(' else set([k-1 for k in temp if k-1 >= 0]))
    return 0 in temp