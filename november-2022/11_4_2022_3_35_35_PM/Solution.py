# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
  def reverseVowels(self, s: str) -> str:
    stack = []
    vow = set(["a", "e", "i", "o", "u"])
    for c in s:
      if c.lower() in vow:
        stack.append(c)
    arr = [c for c in s]
    for i in range(len(arr)):
      if arr[i].lower() in vow: 
        arr[i] = stack.pop()
    return ''.join(arr)
