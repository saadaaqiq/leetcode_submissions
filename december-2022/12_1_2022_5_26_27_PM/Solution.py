# https://leetcode.com/problems/delete-and-earn

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr = sorted([(k,k*count) for k,count in Counter(nums).items()], key= lambda x:x[0])
        dp = [0]*(len(arr)+2)
        for i in range(len(arr)):
            dp[i+2] = max(arr[i][1] + dp[i], dp[i+1]) if i > 0 and arr[i][0] == arr[i-1][0] + 1 else arr[i][1] + dp[i+1]
        return dp[-1]
            