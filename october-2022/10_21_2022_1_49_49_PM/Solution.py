# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    s = set()
    q = deque()
    for i, num in enumerate(nums):
      if i > k:
        v = q.popleft()
        s.remove(v)
      if num in s:
        return True
      else:
        s.add(num)
        q.append(num)
    return False