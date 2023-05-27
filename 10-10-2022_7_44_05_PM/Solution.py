# https://leetcode.com/problems/break-a-palindrome

class Solution:
  def breakPalindrome(self, palindrome: str) -> str:
    res = [c for c in palindrome]
    i = 0
    c = -1
    if len(res)%2 != 0:
      c = len(res)//2
    while i < len(res):
      if res[i] != "a" and i != c:
        res[i] = "a"
        return ''.join(res)
      i += 1
    j = len(res)-1
    while j >= 0:
      if res[j] == "a" and j != c:
        res[j] = "b"
        return ''.join(res)
      j -= 1
    return ""