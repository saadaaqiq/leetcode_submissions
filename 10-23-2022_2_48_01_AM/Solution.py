# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range

class Solution:
  def countOdds(self, l: int, h: int) -> int:
    return (h+h%2-l+l%2)//2
    
    