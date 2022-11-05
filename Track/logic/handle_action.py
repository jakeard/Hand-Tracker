import cv2
import mediapipe as mp
from logic.finger import Finger
from logic.mouse_actions import Mouse_Actions
import autoit
import pyautogui
import numpy as np
import pydirectinput as pdi


pdi.PAUSE = 0

class Handle_Action:
    def __init__(self, fingers):
        self._fingers = fingers
        self._thumb = fingers[0]
        self._pointer = fingers[1]
        self._middle = fingers[2]
        self._ring = fingers[3]
        self._pinky = fingers[4]
        # self._can_click_left = True
        # self._can_click_right = True
        # self._actions = self._set_action_list()
        self._mouse_actions = Mouse_Actions(self._fingers)
        # self.prev_pos = (0, 0) 
    
    # def _set_action_list(self):
    #     actions = {}
    #     actions['move'] = 'pointer'
    #     actions['left_click'] = ['pointer', 'thumb']
    #     actions['right_click'] = ['pointer', 'middle']
    #     actions['scroll_up'] = ['pointer', 'pinky']
    #     actions['scroll_down'] = ['pointer', 'middle', 'ring', 'pinky']

        # return actions
        

    def check(self, hands):
        # hand = hands[0]
        open = self._get_open_fingers()
        
        # w = self._middle.get_specific_pos('top')[0]
        # m = self._pointer.get_specific_pos('top')[0]
        # print(w - m)
        
        # print(self._middle.get_specific_pos('top')[0] - self._pointer.get_specific_pos('top')[0])
        self._mouse_actions.check_match(open)
        # self._keyboard_Actions.check_match(open2)
        # self._check_move_mouse(open)
        # self._check_left_click(open)
        # self._check_right_click(open)
        # self._check_scroll_up(open)
    
    def _get_open_fingers(self):
        open = [x.get_name() for x in self._fingers if x.get_specific_pos('top')[1] < x.get_specific_pos('mid')[1] and x.get_name() != 'thumb']
        if self._thumb.get_specific_pos('top')[0] <= self._pointer.get_specific_pos('base')[0] - 20:
            open.append('thumb')

        # if 'thumb' not in open:
        #     self._can_click_left = True
        # if 'pinky' not in open:
        #     self._can_click_right = True
        
        return open
    
    # def _check_move_mouse(self, open):
    #     # if open == ['pointer']:
    #     if open == ['pointer']:
    #         self._mouse_actions.move()
    
    # def _check_left_click(self, open):
    #     if open == ['pointer', 'thumb']:
    #     # if self._open_match(open, 'thumb'):
    #     # if self._thumb.get_specific_pos('top')[1] > self._pointer.get_specific_pos('mid')[1] and self._can_click:
    #         self._can_click_left = False
    #         self._mouse_actions.click('left')

    # def _check_right_click(self, open):
    #     if open == ['pointer', 'middle']:
    #         self._can_click_right = False
    #         self._mouse_actions.click('right')
    
    # def _check_scroll_up(self, open):
    #     if open == ['pointer', 'ring']:
    #         pass