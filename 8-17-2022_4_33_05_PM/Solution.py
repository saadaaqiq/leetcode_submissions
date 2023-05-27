# https://leetcode.com/problems/unique-morse-code-words

class Solution:
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    for i,word in enumerate(words):
      w = ''
      for c in word:
        w += morse[ord(c)-97]
      words[i] = w
    
    def wordToInt(s):
      n = 0
      for i, c in enumerate(s):
        if c == '-':
          n = n|1<<i
      return n
    
    myset = set()
    
    for word in words:
      myset.add(wordToInt(word))
      
    return len(myset)