# https://leetcode.com/problems/valid-word-abbreviation

class Solution:
  def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    k, i = 0, 0
    while k < len(word) and i < len(abbr):
      if not abbr[i].isnumeric():
        if abbr[i] != word[k]:
          return False
        i += 1
        k += 1
      elif abbr[i] == "0":
        return False
      else:
        j = i + 1
        num = abbr[i]
        while j < len(abbr) and abbr[j].isnumeric():
          num += abbr[j]
          j += 1
        i = j
        k += int(num)
        if k > len(word):
          return False
    return k == len(word) and i == len(abbr)