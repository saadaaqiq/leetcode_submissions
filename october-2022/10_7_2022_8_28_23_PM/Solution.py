# https://leetcode.com/problems/next-greater-element-i

class Solution:
  def nextGreaterElement(self, subset, wholeset):
    dic = {v:i for i,v in enumerate(subset)}
    mono = []
    ans = [-1]*len(subset)
    for w in wholeset:
      if not mono and w in dic:
        mono.append(w)
        continue
      while mono and w > mono[-1]:
        ans[dic[mono.pop()]] = w
      if w in dic:
        mono.append(w)
    return ans
                  