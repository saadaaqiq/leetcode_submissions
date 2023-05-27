# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters

class Solution:
  def modifyString(self, s: str) -> str:
    i = 0
    stri = ''
    while i < len(s):
      if s[i] != '?':
        stri += s[i]
      else:
        k = 97
        while (len(stri)>0 and k == ord(stri[len(stri)-1])) \
            or (i > 0 and s[i-1] != '?' and k == ord(s[i-1])) \
            or (i < len(s) - 1 and s[i+1] != '?' and k == ord(s[i+1])):
          k+=1
        stri += chr(k)
      i+=1
    return stri