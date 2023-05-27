# https://leetcode.com/problems/count-days-spent-together

class Solution:
    def countDaysTogether(self, aA: str, lA: str, aB: str, lB: str) -> int:
        arr = [0] + [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1,13):
            arr[i] = arr[i] + arr[i-1]
        x, y = [arr[int(aA[:2])-1] + int(aA[3:]), arr[int(lA[:2])-1] + int(lA[3:])], [arr[int(aB[:2])-1] + int(aB[3:]), arr[int(lB[:2])-1] + int(lB[3:])]
        return len(set(range(x[0], x[1]+1)).intersection(set(range(y[0], y[1]+1))))
        
        