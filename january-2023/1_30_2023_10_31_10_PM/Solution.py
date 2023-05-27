# https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, arr: List[List[int]], I: List[int]) -> List[List[int]]:
        if not arr:
            return [I]
        x = bisect_left([interval[1] for interval in arr], I[0])
        y = bisect_right([interval[0] for interval in arr], I[1])
        print((x,y))
        return arr[:x] + [[min(I[0], arr[x][0] if x < len(arr) else math.inf), max(I[1], arr[y-1][1] if 0<=y-1<len(arr) else -math.inf) ]] + arr[y:]


            
        
        