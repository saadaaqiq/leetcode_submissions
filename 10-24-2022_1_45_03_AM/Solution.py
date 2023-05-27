# https://leetcode.com/problems/richest-customer-wealth

class Solution:
  def maximumWealth(self, accounts: List[List[int]]) -> int:
    for i in range(len(accounts)):
      for j in range(len(accounts[0])):
        if j > 0:
          accounts[i][j] += accounts[i][j-1]
    m = -float("infinity")
    for i in range(len(accounts)):
      if accounts[i][-1] > m:
        m = accounts[i][-1]
    return m