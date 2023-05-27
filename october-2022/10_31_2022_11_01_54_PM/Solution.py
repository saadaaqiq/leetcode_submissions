# https://leetcode.com/problems/earliest-possible-day-of-full-bloom

class Solution:
  def earliestFullBloom(self, plantTime: List[int], growthTime: List[int]) -> int:
    mini, time = -float("infinity"), 0 
    for gT, pT in sorted(zip(growthTime, plantTime), reverse=True): time, mini = time + pT, max(mini, time + pT + gT)
    return mini
                        
    
    