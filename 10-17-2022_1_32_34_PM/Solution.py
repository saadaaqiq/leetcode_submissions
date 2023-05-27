# https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution:
  def checkIfPangram(self, sentence: str) -> bool:
    arr = [False for i in range(26)]
    k = 0
    for c in sentence:
      if not arr[ord(c)-97]:
        arr[ord(c)-97] = True
        k += 1
      if k == 26:
        return True
    return False