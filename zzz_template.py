class Robot(DobotControl):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    dobot = Robot()
    dobot.setAddr(Robot.search()[0])
    dobot.startRobot()

### Write Your Code Here ######################################################
# dobot.moveTo(x, y, z, r) # Absolute Position
# dobot.moveInc(dx, dy, dz, dr) # Relative Position
# dobot.setPump(17, 18) # Active Pump
# dobot.resetPump(17, 18) # Deactive Pump
# dobot.suck() # S U C K
# dobot.unsuck # un S U C K
# time.sleep(1) # sleep 1 sec

class DC: # Dobot Camera offset to 0-100 percent
    def __init__(self): # target cam pixel
        self.dobot_min_x = 197.1 # 'dobot west most'
        self.dobot_max_x = 369.1 # 'dobot east most'
        self.dobot_min_y = -79.2 # 'dobot south most'
        self.dobot_max_y =  99.8 #'dobot north most'
        self.dobot_min_z = 100 # 'dobot bottom most'
        self.dobot_max_z = 150 # 'dobot upper most'
        self.cam_min_x =  81 # 'cam west most'
        self.cam_max_x = 252 # 'cam east most'
        self.cam_min_y =  32 # 'cam north most'
        self.cam_max_y = 206 # 'cam south most'
        self.dobot_dif_x = self.dobot_max_x - self.dobot_min_x # WorkSpace size
        self.dobot_dif_y = self.dobot_max_y - self.dobot_min_y
        self.cam_dif_x = self.cam_max_x - self.cam_min_x
        self.cam_dif_y = self.cam_max_y - self.cam_min_y
        # !!! opencv cam flip Y axis (pixel 0 at top)
        # webcam -> dobot --> rotate 180 degree

    def cam2botX(self,camX):
        camX = (self.cam_dif_x - (camX - self.cam_min_x)) / self.cam_dif_x
        botX = (camX * self.dobot_dif_x) + self.dobot_min_x
        return  botX
    
    def cam2botY(self,camY):
        camY = (self.cam_dif_y - (camY - self.cam_min_y)) / self.cam_dif_y 
        camY = 1 - camY # opencv cam flip Y
        botY = (camY * self.dobot_dif_y) + self.dobot_min_y
        return  botY
        
aaaa = DC()
print(aaaa.cam2bot(81,206))

dobot.moveTo(aaaa.cam2bot(81,206)[0], aaaa.cam2bot(81,206)[1], 48, 40) # Absolute Position
time.sleep(3) # sleep 1 sec

# Top Left :  97,  43 ___	344.1000  -78.4000
# Top Right: 219,  43 ___	216.0000  -78.4000
# Bot Left :  97, 193 ___   344.1000   78.8000
# Bot Right: 219, 193 ___   216.0000   78.8000