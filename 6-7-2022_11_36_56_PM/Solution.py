# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters

class Solution:
  def modifyString(self, s: str) -> str:
    i = 0
    stri = ''
    while i < len(s):
      if s[i] != '?':
        stri += s[i]
      else:
        neighbours = set()
        if len(stri)>0:
          neighbours.add(ord(stri[len(stri)-1]))
        if i > 0 and s[i-1] != '?': 
          neighbours.add(ord(s[i-1]))
        if i < len(s) - 1 and s[i+1] != '?':
          neighbours.add(ord(s[i+1]))
        k = 97
        while k in neighbours:
          k+=1
        stri += chr(k)
      i+=1
    return stri