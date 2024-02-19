import time

import DobotAPI
import DobotTypes
from DobotControl import DobotControl

class Robot(DobotControl):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    dobot = Robot()
    dobot.setAddr(Robot.search()[0])
    dobot.startRobot()

    #Write Your Code Here

dobot.moveInc(0, 0, 50, 0) # Relative Position


