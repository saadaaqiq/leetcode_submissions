# https://leetcode.com/problems/earliest-possible-day-of-full-bloom

class Solution:
  def earliestFullBloom(self, plantTime: List[int], growthTime: List[int]) -> int:
    def comp(a, b): return (a[0] + max(a[1], b[0]+b[1])) - (b[0] + max(b[1], a[0]+a[1]))
    totalTimes, latest, current = sorted(list(zip(plantTime, growthTime)), key=cmp_to_key(comp)), 0, 0
    for pTime, gTime in totalTimes: latest, current = max(latest, pTime + gTime + current), current + pTime
    return latest
    