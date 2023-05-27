# https://leetcode.com/problems/reduce-array-size-to-the-half

class Solution:
  def minSetSize(self, arr: List[int]) -> int:
    n = len(arr)
    dic = {}
    for num in arr:
      if num not in dic:
        dic[num] = 1
      else:
        dic[num] += 1
    vals = sorted(list(dic.values()))
    c = len(vals)-1
    while n > len(arr)/2:
      n -= vals[c]
      c -= 1
    return len(vals)-1-c
    
      