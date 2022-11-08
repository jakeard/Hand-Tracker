# import cv2
# import mediapipe as mp
# from logic.finger import Finger
from logic.mouse_actions import Mouse_Actions
from logic.keyboard_actions import Keyboard_Actions
# import autoit
# import pyautogui
# import numpy as np
# import pydirectinput as pdi


# pdi.PAUSE = 0

class Handle_Action:
    def __init__(self, hand1, hand2):
        # self._fingers = fingers
        # self._thumb = fingers[0]
        # self._pointer = fingers[1]
        # self._middle = fingers[2]
        # self._ring = fingers[3]
        # self._pinky = fingers[4]
        # self._can_click_left = True
        # self._can_click_right = True
        # self._actions = self._set_action_list()
        self._unpack_hands(hand1, hand2)
        self._mouse_actions = Mouse_Actions(hand1)
        self._keyboard_actions = Keyboard_Actions(hand2)

    def _unpack_hands(self, hand1, hand2):
        self._fingers1 = hand1
        self._thumb1 = hand1[0]
        self._pointer1 = hand1[1]
        self._middle1 = hand1[2]
        self._ring1 = hand1[3]
        self._pinky1 = hand1[4]
        self._fingers2 = hand2
        self._thumb2 = hand2[0]
        self._pointer2 = hand2[1]
        self._middle2 = hand2[2]
        self._ring2 = hand2[3]
        self._pinky2 = hand2[4]
    
    # def _set_action_list(self):
    #     actions = {}
    #     actions['move'] = 'pointer'
    #     actions['left_click'] = ['pointer', 'thumb']
    #     actions['right_click'] = ['pointer', 'middle']
    #     actions['scroll_up'] = ['pointer', 'pinky']
    #     actions['scroll_down'] = ['pointer', 'middle', 'ring', 'pinky']

        # return actions
        

    def check(self, hand):
        # hand = hands[0]
        open = self._get_open_fingers(hand)
        # open1, open2 = self._get_open_fingers()
        
        # w = self._middle.get_specific_pos('top')[0]
        # m = self._pointer.get_specific_pos('top')[0]
        # print(w - m)
        
        # print(self._middle.get_specific_pos('top')[0] - self._pointer.get_specific_pos('top')[0])
        
        
        
        if hand == 'Right':
            self._mouse_actions.check_match(open) # THIS NEEDS TO BE WORKED ON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        else:
            self._keyboard_actions.check_match(open)


        # self._check_move_mouse(open)
        # self._check_left_click(open)
        # self._check_right_click(open)
        # self._check_scroll_up(open)
    
    def _get_open_fingers(self, fingers):
        open = [x.get_name() for x in fingers if x.get_specific_pos('top')[1] < x.get_specific_pos('mid')[1] and x.get_name() != 'thumb']
        # open1 = self.find_open(self._fingers1)
        if fingers[0].get_specific_pos('top')[0] <= fingers[1].get_specific_pos('base')[0] - 50:
            open.append('thumb')
        # open2 = [x.get_name() for x in self._fingers2 if x.get_specific_pos('top')[1] < x.get_specific_pos('mid')[1] and x.get_name() != 'thumb']
        # if self._thumb2.get_specific_pos('top')[0] <= self._pointer2.get_specific_pos('base')[0] + 50:
        #     open2.append('thumb')

        # if 'thumb' not in open:
        #     self._can_click_left = True
        # if 'pinky' not in open:
        #     self._can_click_right = True
        
        return open
        # return open1, open2
    
    # def find_open(self, fingers):
        # return [x.get_name() for x in fingers if x.get_specific_pos('top')[1] < x.get_specific_pos('mid')[1] and x.get_name() != 'thumb']
    
    # def open_right(self):
    #     return self._thumb1.get_specific_pos('top')[0] <= self._pointer1.get_specific_pos('base')[0] - 50:
    
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