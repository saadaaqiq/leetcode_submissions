# https://leetcode.com/problems/group-anagrams

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dic = {}
    for s in strs:
      t = ''.join(sorted(s))
      if t not in dic:
        dic[t] = []
      dic[t].append(s)
    return list(dic.values())