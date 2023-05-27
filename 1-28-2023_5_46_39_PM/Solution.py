# https://leetcode.com/problems/asteroid-collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr = []
        for x in asteroids:
            insert = True
            while arr and arr[-1] > 0 and x < 0:
                if abs(arr[-1]) <= abs(x):
                    y = arr.pop()
                    if y == -x:
                        insert = False
                        break
                else:
                    insert = False
                    break
            if insert:
                arr.append(x)
        return arr