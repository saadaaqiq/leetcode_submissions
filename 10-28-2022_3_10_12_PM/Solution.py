# https://leetcode.com/problems/valid-palindrome

class Solution:
  def isPalindrome(self, s: str) -> bool:
    i, j = 0, len(s)-1
    letters = set("0123456789abcdefghijklmnopqrstuvwxyz")
    while i < j:
      if s[i].lower() not in letters: 
        i += 1
      elif s[j].lower() not in letters: 
        j -= 1
      elif s[i].lower() != s[j].lower():
        return False
      else:
        i += 1
        j -= 1
    return True