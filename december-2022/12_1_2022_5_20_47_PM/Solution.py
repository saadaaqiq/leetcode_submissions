# https://leetcode.com/problems/delete-and-earn

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        arr = [(k,k*count[k]) for k in count]
        arr.sort(key=lambda x:x[0])
        n = len(arr)
        dp = [0]*(n+2)
        for i in range(n):
            dp[i+2] = max(arr[i][1] + dp[i], dp[i+1]) if i > 0 and arr[i][0] == arr[i-1][0] + 1 else arr[i][1] + dp[i+1]
        return dp[-1]
            