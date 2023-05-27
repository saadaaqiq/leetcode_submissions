# https://leetcode.com/problems/missing-ranges

class Solution:
  def findMissingRanges(self, arr, lower, upper):
    i, k, missing = 0, lower, []
    while k < upper + 1:
      if i == len(arr):
        missing.append(str(k)+"->"+str(upper) if k!=upper else str(k))
        break
      if k < arr[i]:
        missing.append(str(k)+"->"+str(arr[i]-1) if k!=arr[i]-1 else str(k))
      k = arr[i] + 1
      i += 1
    return missing