# https://leetcode.com/problems/minimum-penalty-for-a-shop

class Solution:
    def bestClosingTime(self, customers: str) -> int:
      n = len(customers)
      dp1 = [0] * (n+1)
      dp2 = [0] * (n+1)
      for i in range(n-1, -1, -1):
        dp1[i] += dp1[i+1]
        if customers[i] == "Y":
          dp1[i] += 1
      for i in range(1, n+1):
        dp2[i] += dp2[i-1]
        if customers[i-1] == "N":
          dp2[i] += 1
      for i in range(n+1):
        dp1[i] += dp2[i]
      mini, ind = float("infinity"), -1
      for i in range(n+1):
        if dp1[i] < mini:
          mini = dp1[i]
          ind = i
      return ind