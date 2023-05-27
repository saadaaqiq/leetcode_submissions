# https://leetcode.com/problems/palindrome-permutation

class Solution:
  def canPermutePalindrome(self, s: str) -> bool:
    dic = { chr(i): 0 for i in range(97, 97+26) }
    for c in s:
      dic[c] += 1
    if len(s)%2==0:
      for k in dic:
        if dic[k]%2==1:
          return False
    else:
      t = 0
      for k in dic:
        if dic[k]%2==1:
          if t == 0:
            t+=1
          else:
            return False
    return True