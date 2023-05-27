# https://leetcode.com/problems/top-k-frequent-elements

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    res = []
    dic = {}
    dct = {}
    
    for num in nums:
      if num not in dic:
        dic[num] = 0
      dic[num] += 1  
        
    for ky in dic:
      if dic[ky] not in dct:
        dct[dic[ky]] = []
      dct[dic[ky]].append(ky)
    
    keys = list(dct.keys())
    keys = [ -ky for ky in keys ]
    heapq.heapify(keys)

    while len(res)<k:
      if keys:
        n = -heapq.heappop(keys)
        res+=dct[n]
      else:
        break
      
    return res

    