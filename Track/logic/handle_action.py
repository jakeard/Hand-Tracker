import cv2
import mediapipe as mp
from logic.finger import Finger

class Handle_Action:
    def __init__(self, fingers):
        self.fingers = fingers
        self.thumb = fingers[0]
        self.pointer = fingers[1]
        self.middle = fingers[2]
        self.ring = fingers[3]
        self.pinky = fingers[4]

        self.check()
        # self.unpack(fingers)
        # self.thumb, self.pointer, self.middle, self.ring, self.pinky = self.unpack(fingers)
        

    def check(self):
        open = [x.get_name() for x in self.fingers if x.get_pos()[3][1] < x.get_pos()[1][1]]
        if open == ['thumb', 'pointer']:
            self.move_mouse()
    
    def move_mouse(self):
        pass