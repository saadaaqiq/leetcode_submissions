# https://leetcode.com/problems/earliest-possible-day-of-full-bloom

class Solution:
  def earliestFullBloom(self, plantTime: List[int], growthTime: List[int]) -> int:
    
    
    
    
    def comp(p1, p2):
      ptime1, gtime1 = p1
      ptime2, gtime2 = p2
      return (ptime1 + max(gtime1, ptime2+gtime2)) - (ptime2 + max(gtime2, ptime1+gtime1))
    
    totalTimes = list(zip(plantTime, growthTime))
    totalTimes.sort(key=cmp_to_key(comp))
    print(totalTimes)
    
    latest = 0
    current = 0
    for pTime, gTime in totalTimes:
      latest = max(latest, pTime + gTime + current)
      current += pTime
    
    return latest
    