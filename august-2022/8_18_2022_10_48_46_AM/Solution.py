# https://leetcode.com/problems/reduce-array-size-to-the-half

class Solution:
  def minSetSize(self, arr: List[int]) -> int:
    n = len(arr)
    c = 0
    dic = { num : 0 for num in arr }
    for num in arr:
      dic[num] += 1
    print(dic)
    vals = sorted(list(dic.values()),reverse=True)    
    while n > math.ceil(len(arr)/2):
      n -= vals[c]
      c += 1
    return c
    
      