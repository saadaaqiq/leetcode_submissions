# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

class Solution:
  def maxLength(self, arr: List[str]) -> int:
    
    def dfs(i, notallowed):
      if i == len(arr):
        return len(notallowed)
      if len(set(arr[i])) != len(arr[i]) or len(set(arr[i]).intersection(notallowed)) != 0:
        return dfs(i+1, notallowed)
      return max([dfs(j, notallowed.union(set(arr[i]))) for j in range(i+1, len(arr))]) if i < len(arr)-2 else dfs(i+1, notallowed.union(set(arr[i])))
      
    return max([dfs(i, set()) for i in range(len(arr))])
    
    
    
    
    
    