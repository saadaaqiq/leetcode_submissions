# https://leetcode.com/problems/robot-room-cleaner

class Solution:       
    def cleanRoom(self, robot):            
        vis = set()
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]

        def rec(i, j, d):
            vis.add((i,j))
            robot.clean()
            for index in range(4):
                # direction robot came from then check clockwise
                new_d = (d + index) % 4 
                r, c = i + dirs[new_d][0], j + dirs[new_d][1]
                if (r,c) not in vis and robot.move():
                    rec(r,c,new_d)
                    for k in range(2): robot.turnRight()
                    robot.move()
                    for k in range(2): robot.turnRight()
                robot.turnRight()
            
        rec(0,0,0)