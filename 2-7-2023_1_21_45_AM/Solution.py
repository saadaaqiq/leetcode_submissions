# https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        vis = set()
        n = len(arr)
        while q:
            ind = q.popleft()
            if arr[ind] == 0:
                return True
            vis.add(ind)
            if ind - arr[ind] >= 0 and ind - arr[ind] not in vis:
                q.append(ind - arr[ind])
            if ind + arr[ind] < n and ind + arr[ind] not in vis:
                q.append(ind + arr[ind])
        return False