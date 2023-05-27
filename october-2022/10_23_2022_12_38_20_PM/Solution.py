# https://leetcode.com/problems/valid-palindrome-ii

class Solution:
  def validPalindrome(self, s: str) -> bool:
    l, r = 0, len(s)-1
    while l <= r:
      if s[l]!=s[r]:
        break
      l += 1
      r -= 1
    nl,tr = l+1, r
    tl, nr = l, r-1
    b1, b2 = True, True
    while nl<=tr:
      if s[nl]!=s[tr]:
        b1 = False
        break
      nl+=1
      tr-=1
    while tl<=nr:
      if s[tl]!=s[nr]:
        b2 = False
        break
      tl+=1
      nr-=1
    return b1 or b2