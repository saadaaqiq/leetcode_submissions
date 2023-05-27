# https://leetcode.com/problems/unique-morse-code-words

class Solution:
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    myset = set()
    for word in words:
      k = 0
      n = 0
      for c in word:
        m = morse[ord(c)-97]
        for l in m:
          if l == '-':
            n = n|1<<k
          k += 1
      myset.add(n)
    return len(myset)
    