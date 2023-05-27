# https://leetcode.com/problems/ransom-note

class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    mag = Counter(magazine)
    for c in ransomNote:
      if c not in mag or mag[c] == 0:
        return False
      mag[c] -= 1
    return True