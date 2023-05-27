# https://leetcode.com/problems/robot-room-cleaner

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        
        def move_up():
            b = robot.move()
            return b 
            
        def move_right():
            robot.turnRight()
            b = robot.move()
            robot.turnLeft()
            return b

        def move_down():
            robot.turnRight()
            robot.turnRight()
            b = robot.move()
            robot.turnLeft()
            robot.turnLeft()
            return b

        def move_left():
            robot.turnLeft()
            b = robot.move()
            robot.turnRight()
            return b

        vis = set()

        def dfs(i,j):
            robot.clean()
            vis.add((i,j))

            if (i-1,j) not in vis:
                if move_up():
                    dfs(i-1, j)
                    move_down()
            
            if (i,j+1) not in vis:
                if move_right():
                    dfs(i, j+1)
                    move_left()

            if (i+1,j) not in vis:
                if move_down():
                    dfs(i+1, j)
                    move_up()
            
            if (i, j-1) not in vis:
                if move_left():
                    dfs(i, j-1)
                    move_right()
            
        dfs(0,0)               

