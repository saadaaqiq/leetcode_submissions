# https://leetcode.com/problems/maximum-profit-in-job-scheduling

class Solution:
    def jobScheduling(self, starts, ends, profits):
      n = len(profits)
      arr = sorted(list(zip(starts, ends, profits)))
      starts.sort()

      @lru_cache
      def rec(i):
        if i == n: return 0
        # here we have 2 cases:
        # either use job i or not

        # case 1: using job i
        a = arr[i][2] # this is the profit from job i 
        j = bisect_left(starts, arr[i][1])
        a += rec(j) # adding the profit from the first job that starts after job i ends
        # case 2: skipping to next job
        b = rec(i+1) 
        return max(a, b)

      return rec(0)