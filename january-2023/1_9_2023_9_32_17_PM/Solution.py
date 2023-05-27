# https://leetcode.com/problems/minimum-costs-using-the-train-line

class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        arr = [[0,expressCost]]
        for i in range(n):
            arr.append([min(arr[-1][0]+expressCost+express[i], arr[-1][0]+regular[i], arr[-1][1]+express[i]), min(arr[-1][0]+regular[i]+expressCost,arr[-1][0]+expressCost+express[i], arr[-1][1]+express[i])])
        return [min(arr[i]) for i in range(1,n+1)]