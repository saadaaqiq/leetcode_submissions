# https://leetcode.com/problems/minimum-time-to-complete-trips

class Solution:
    def minimumTime(self, time: List[int], target: int) -> int:
        time.sort()

        def check_trips(timestamp):
            trips = 0
            for t in time:
                trips += timestamp // t
                if trips >= target:
                    return True
            return False
        
        l, r = 0, 10**20

        while l < r:
            mid = (l+r) // 2
            if check_trips(mid):
                r = mid
            else:
                l = mid + 1

        return l

