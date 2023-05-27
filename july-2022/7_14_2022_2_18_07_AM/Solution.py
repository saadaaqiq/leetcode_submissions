# https://leetcode.com/problems/length-of-last-word

class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    # return len(s.split()[-1])
    old = ''
    potential = ''
    for i in range(len(s)):
      if s[i] == ' ':
        if len(potential)>0:
          old = potential
          potential = ''
      else:
        potential += s[i]
    return len(potential) if len(potential)>0 else len(old)