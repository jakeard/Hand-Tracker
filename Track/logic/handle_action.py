import cv2
import mediapipe as mp
from logic.finger import Finger
# import autoit
import pyautogui
import pydirectinput as pdi
from logic import constants

pdi.PAUSE = 0

class Handle_Action:
    def __init__(self, fingers):
        self.fingers = fingers
        self.thumb = fingers[0]
        self.pointer = fingers[1]
        self.middle = fingers[2]
        self.ring = fingers[3]
        self.pinky = fingers[4]
        

    def check(self):
        open = [x.get_name() for x in self.fingers if x.get_pos()[3][1] < x.get_pos()[1][1]]
        if open == ['thumb', 'pointer']:
            self.move_mouse()
    
    def move_mouse(self):
        (x, y) = self.pointer.get_specific_pos('top')
        pdi.moveTo(x * 3, y)