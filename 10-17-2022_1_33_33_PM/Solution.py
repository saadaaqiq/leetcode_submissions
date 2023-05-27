# https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution:
  def checkIfPangram(self, sentence: str) -> bool:
    return len({c for c in sentence}) == 26