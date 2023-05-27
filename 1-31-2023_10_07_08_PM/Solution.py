# https://leetcode.com/problems/best-team-with-no-conflicts

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        arr = sorted(zip(scores, ages))
        dp = [arr[i][0] for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if arr[j][1] >= arr[i][1]:
                    dp[i] = max(dp[i], arr[i][0] + dp[j])
        return max(dp)
            

        