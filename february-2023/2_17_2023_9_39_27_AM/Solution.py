# https://leetcode.com/problems/traffic-light-controlled-intersection

import threading 

class TrafficLight:
    def __init__(self):
        self.curr_green = 1
        self.light_lock = threading.Lock()

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        with self.light_lock: 
            if self.curr_green != roadId:
                turnGreen()
                self.curr_green = roadId
            crossCar()        