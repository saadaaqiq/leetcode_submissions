# https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    count = Counter(arr)
    return len(set(count.keys())) == len(set(count.values()))