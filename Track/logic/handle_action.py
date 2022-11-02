import cv2
import mediapipe as mp
from logic.finger import Finger
from logic.mouse_actions import Mouse_Actions
import autoit
import pyautogui
import numpy as np
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
        self.mouse_actions = Mouse_Actions(self.fingers)
        # self.prev_pos = (0, 0) 
        

    def check(self, hands):
        hand = hands[0]
        open = [x.get_name() for x in self.fingers if x.get_specific_pos('top')[1] < x.get_specific_pos('low')[1]]
        # if hand == 'Right':
        #     if self.thumb.get_specific_pos('top')[0] < self.pointer.get_specific_pos('base')[0]:
        #         open.append('thumb')
        # else:
        #     if self.thumb.get_specific_pos('top')[0] > self.pointer.get_specific_pos('base')[0]:
        #         open.append('thumb')
        print(open)
        if open == ['thumb', 'pointer']:
            # self.move_mouse()
            self.mouse_actions.move_mouse()
    
    # def move_mouse(self):
    #     (x, y) = self.pointer.get_specific_pos('top')
    #     x = round(np.interp(x, (150, 490), (0, 1920)))
    #     y = round(np.interp(y, (100, 380), (0, 1920)))
    #     # print(f"x: {x}, y: {y}\n")
    #     # print(x, y)
    #     # curx = round(self.prev_pos[0] + (x - self.prev_pos[0]) / 5)
    #     # cury = round(self.prev_pos[1] + (y - self.prev_pos[1]) / 5)
    #     # print(curx, cury)
    #     # diff_x = self.prev_pos[0] - x
    #     # diff_y = self.prev_pos[1] - y
    #     # first_x = x
    #     # first_y = y
    #     # if self.prev_pos[0] > x:
    #     #     first_x = x + 1
    #     # elif self.prev_pos[0] < x:
    #     #     first_x = x - 1

    #     # if self.prev_pos[1] > y:
    #     #     first_y = y + 1
    #     # elif self.prev_pos[1] < y:
    #     #     first_y = y - 1

        
        
    #     # autoit.mouse_move(x - 2, y - 2, 0)
    #     # autoit.mouse_move(x - 1, y - 1, 0)
    #     # autoit.mouse_move(first_x, first_y, 0)
    #     autoit.mouse_move(x, y, 0)
    #     # autoit.mouse_move(curx, cury, 0)
    #     # self.prev_pos = (x, y)
    #     # pdi.moveTo(x, y)