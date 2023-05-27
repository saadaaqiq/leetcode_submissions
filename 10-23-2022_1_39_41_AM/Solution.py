# https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    count = Counter(arr)
    return len(count) == len(set(count.values()))