# https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        A, B = costs[:n], costs[n:]
        a, b = sum([x[0] for x in A]), sum([x[1] for x in B])

        while True:
            boo = False
            for i in range(n):
                for j in range(n):
                    if a - A[i][0] + B[j][0] + b - B[j][1] + A[i][1] < a + b:
                        a = a + B[j][0] - A[i][0]
                        b = b - B[j][1] + A[i][1]
                        A[i][0], A[i][1], B[j][0], B[j][1] = B[j][0], B[j][1], A[i][0], A[i][1]
                        boo = True
            if not boo:
                return a + b


        
