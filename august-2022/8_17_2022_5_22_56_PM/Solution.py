# https://leetcode.com/problems/unique-morse-code-words

class Solution:
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    return len(set([''.join([[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."][ord(c)-97] for c in word]) for word in words]))        