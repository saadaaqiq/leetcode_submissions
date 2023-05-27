# https://leetcode.com/problems/top-k-frequent-elements

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    count = collections.Counter(nums)
    rank = [[] for i in range(n)] 
    for x in count:
      rank[count[x]-1].append(x)
    res = []
    j = 0
    print(rank)
    for i in range(len(nums)-1, -1, -1):
      if rank[i]:
        for x in rank[i]:
          res.append(x)
        j += 1
        if len(res) == k:
          return res
    return res
        
