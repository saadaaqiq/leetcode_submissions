# https://leetcode.com/problems/circular-sentence

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if len(sentence)==1: return True
        if sentence[0] != sentence[-1]: return False
        for i in range(len(sentence)):
          if sentence[i]==" " and i>0 and i<len(sentence)-1:
            if sentence[i-1] != sentence[i+1]:
              return False
        return True