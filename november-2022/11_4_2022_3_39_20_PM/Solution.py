# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
  def reverseVowels(self, s: str) -> str:
    stack = []
    vow = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    for c in s:
      if c in vow:
        stack.append(c)
    res = ""
    for c in s:
      if c in vow: 
        res += stack.pop()
      else:
        res += c
    return res
