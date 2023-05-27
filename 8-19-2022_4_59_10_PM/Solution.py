# https://leetcode.com/problems/single-row-keyboard

class Solution:
  def calculateTime(self, keyboard: str, word: str) -> int:
    place = { k: i for i,k in enumerate(keyboard) }
    return place[word[0]] + sum([abs(place[word[i]] - place[word[i+1]]) for i in range(len(word)-1)])