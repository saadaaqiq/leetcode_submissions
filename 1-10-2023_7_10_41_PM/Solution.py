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
        
        def move_dir(direction):
            for i in range(direction): robot.turnRight()
            b = robot.move()
            for i in range(direction): robot.turnLeft()
            return b

        vis = set()

        def dfs(i,j):
            robot.clean()
            vis.add((i,j))
            if (i-1,j) not in vis and move_dir(0):
                dfs(i-1, j)
                move_dir(2)
            if (i,j+1) not in vis and move_dir(1):
                dfs(i, j+1)
                move_dir(3)
            if (i+1,j) not in vis and move_dir(2):
                dfs(i+1, j)
                move_dir(0)
            if (i, j-1) not in vis and move_dir(3):
                dfs(i, j-1)
                move_dir(1)
            
        dfs(0,0)               

