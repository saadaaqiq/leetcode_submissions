# https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        starting = 0
        total, current = 0, 0
        for i in range(n):
            current += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if current < 0:
                current, starting = 0, i+1
        return starting%n if total>=0 else -1


        


            