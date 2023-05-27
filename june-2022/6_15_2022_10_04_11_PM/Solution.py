# https://leetcode.com/problems/shortest-word-distance

class Solution:
  def shortestDistance(self, words: List[str], w1: str, w2: str) -> int:
    mini = len(words)
    last_w1, last_w2 = -1, -1
    for i, word in enumerate(words):
      if word == w1:
        last_w1 = i
      if word == w2:
        last_w2 = i
      if last_w1 >= 0 and last_w2 >= 0:
        mini = min(mini, abs(last_w1 - last_w2))
    return mini
    