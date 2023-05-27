# https://leetcode.com/problems/4-keys-keyboard

class Solution:
  def maxA(self, n: int) -> int:
    dic = {}
    
    def dfs(p, num, sel):
      if p <= 2:
        if (p, num, sel) not in dic:
          dic[(p, num, sel)] = num + p * sel
        return dic[(p, num, sel)]
      if (p-1, num + sel, sel) not in dic:
        dic[(p-1, num + sel, sel)] = dfs(p-1, num + sel, sel)
      if (p-3, 2 * num, num) not in dic:
        dic[(p-3, 2 * num, num)] = dfs(p-3, 2 * num, num)
      return max(dic[(p-1, num + sel, sel)], dic[(p-3, 2 * num, num)])
      
    return dfs(n, 0, 1)