# https://leetcode.com/problems/hand-of-straights

class Solution:
  def isNStraightHand(self, hand: List[int], n: int) -> bool:

    if len(hand) % n != 0:
      return False

    heapq.heapify(hand)
        
    while hand:
      old = heapq.heappop(hand)
      cache = []
      c = 1
      while hand and c < n:
        new = heapq.heappop(hand)
        if new == old:
          cache.append(new)
        elif new != old + 1:
          return False
        else:
          c += 1
          old = new
      if not hand and c < n:
        return False
      while cache:
        heapq.heappush(hand, cache.pop())
    
    return True