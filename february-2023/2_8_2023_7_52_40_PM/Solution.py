# https://leetcode.com/problems/jump-game-iv

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        N = len(nums)
        
        if N <= 1:
            return 0
    
        lookup = collections.defaultdict(list)
        i = 0
        
        while i < N:
            j = i
            while j < N and nums[j] == nums[i]:
                j += 1
            lookup[nums[i]].append(i)
            if j > i + 1:
                lookup[nums[i]].append(j-1)
            i = j
        

        left_to_right = set([0])
        vis = {0, N-1}
        step = 0
        right_to_left = set([N-1])

        while left_to_right:
            if len(left_to_right) > len(right_to_left):
                left_to_right, right_to_left = right_to_left, left_to_right
            next_set = set()

            # same values
            for i in left_to_right:
                for j in lookup[nums[i]]:
                    if j in right_to_left:
                        return step + 1
                    if j not in vis:
                        vis.add(j)
                        next_set.add(j)
                # clear to not search again
                lookup[nums[i]].clear()
                # check neighbors
                for dx in [-1, 1]:
                    if i + dx in right_to_left:
                        return step + 1
                    if 0 <= i + dx < N and i + dx not in vis:
                        vis.add(i + dx)
                        next_set.add(i + dx)
            
            left_to_right = next_set
            step += 1

        return -1
