# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def reverse_bisect(array, ind):
            l, r = 0, len(array)
            while l < r:
                mid = (l+r)//2
                if nums[ind] > nums[array[mid]]:
                    r = mid
                else:
                    l = mid + 1
            return l

        n = len(nums)
        arr = [[0]]
        pointers = [-1] * n
        
        for i in range(1, n):
            placed = False
            eq = False
            for tab in arr:
                if nums[i] < nums[tab[-1]]:
                    if not eq:
                        tab.append(i)
                    placed = True
                    eq = False
                    break
                elif nums[i] > nums[tab[-1]]:
                    pointers[i] = reverse_bisect(tab, i)
                    if pointers[i] >= len(tab):
                        pointers[i] = -1
                else:
                    eq = True
            if not placed and not eq:
                arr.append([i])
        
        def dfs(index, t):
            print((index, t))
            if pointers[index] == -1:
                return 1
            return dfs(arr[-t-1][pointers[index]], t+1) + 1

        return max([dfs(k, 1) for k in arr[-1]])
            
