# https://leetcode.com/problems/decode-ways

class Solution:
  def numDecodings(self, s: str) -> int:
    dp = [0]*(len(s))+[1]
    for i in range(len(s)-1, -1, -1):
      dp[i] = 0 if s[i]=="0" else dp[i+1]
      if(i<len(s)-1 and s[i]!="0" and 1<=int(s[i]+s[i+1])<=26):
        dp[i] += dp[i+2]         
    return dp[0]
