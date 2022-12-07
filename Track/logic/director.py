import cv2
import mediapipe as mp
# import time
# import numpy as np
# import pyautogui
# import pydirectinput as pdi
# import autoit
# from logic.handle_action import Handle_Action
from logic.finger import Finger
from logic.hand import Hand
from logic.mouse_actions import Mouse_Actions
from logic.keyboard_actions import Keyboard_Actions
from logic.signs import Signs

class Director:
    def __init__(self, todo):
        # self._thumb = Finger('thumb', 'right')
        # self._pointer = Finger('pointer', 'right')
        # self._middle = Finger('middle', 'right')
        # self._ring = Finger('ring', 'right')
        # self._pinky = Finger('pinky', 'right')
        # self._thumb2 = Finger('thumb', 'left')
        # self._pointer2 = Finger('pointer', 'left')
        # self._middle2 = Finger('middle', 'left')
        # self._ring2 = Finger('ring', 'left')
        # self._pinky2 = Finger('pinky', 'left')
        self._hand1 = Hand('Right', self._create_fingers(), 0)
        self._hand2 = Hand('Left', self._create_fingers(), 0)
        # self._hand2 = Hand('Left', [self._thumb2, self._pointer2, self._middle2, self._ring2, self._pinky2])
        self._mouse_actions = Mouse_Actions(self._hand1.get_fingers())
        self._keyboard_actions = Keyboard_Actions(self._hand2.get_fingers())
        self._signs = Signs(self._hand1.get_fingers(), self._hand1.get_palm_loc())
        if todo == 'mouse':
            self._todo = self._mouse_and_key
        else:
            self._todo = self._asl
        # self._todo = todo
        # self._fingers_hand1 = [self._thumb, self._pointer, self._middle, self._ring, self._pinky]
        # self._fingers_hand2 = [self._thumb2, self._pointer2, self._middle2, self._ring2, self._pinky2]
        # self._actions = Handle_Action(self._fingers_hand1, self._fingers_hand2)
    
    def _create_fingers(self):
        return [Finger('thumb'), Finger('pointer'), Finger('middle'), Finger('ring'), Finger('pinky')]

    def _mouse_and_key(self):
        try:
            self._mouse_actions.check_match(self._hand1.get_open())
        except:
            pass
        try:
            self._keyboard_actions.check_match(self._hand2.get_open())
        except:
            pass
    
    def _asl(self):
        try:
            # print(self._hand1.get_open())
            self._signs.get_pos(self._hand1.get_open())
        except:
            pass
    
    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        # (screen_w, screen_h) = pdi.size()
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        mp_draw = mp.solutions.drawing_utils

        while True:
            _, img = cap.read()
            img = cv2.flip(img, 1)
            h, w, _ = img.shape
            img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_RGB)

            if results.multi_hand_landmarks:
                # for hand in results.multi_handedness:
                for i, hand_lmks in enumerate(results.multi_hand_landmarks):
                    if results.multi_handedness[i].classification[0].label == 'Right':
                        curr_hand = self._hand1
                    else:
                        curr_hand = self._hand2
                    tracker = {}
                    count = -1
                    for id, lm in enumerate(hand_lmks.landmark):
                        # print(len(hand_lmks.landmark))
                        lm_x, lm_y, lm_z = int(lm.x * w), int(lm.y * h), lm.z
                        if id % 4 != 1 and count != -1:
                            tracker[count].append((lm_x, lm_y, lm_z))
                        elif count == -1:
                            curr_hand.set_palm_loc((lm_x, lm_y, lm_z))
                            count += 1
                        else:
                            count += 1
                            tracker[count] = [(lm_x, lm_y, lm_z)]
                    mp_draw.draw_landmarks(img, hand_lmks, mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2), mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))
                    self._set_fingers_loc(tracker, curr_hand)
                self._todo()
                
            cv2.imshow("Image", img)
            cv2.waitKey(1)

                # try:
                #     self._mouse_actions.check_match(self._hand1.get_open())
                # except:
                #     pass
                # try:
                #     self._keyboard_actions.check_match(self._hand2.get_open())
                # except:
                #     pass
                # print(curr_hand)
                # try:
                #     # print(self._hand1.get_open())
                #     self._signs.get_pos(self._hand1.get_open())
                # except:
                #     pass
    
    # def run2(self):
    #     cap = cv2.VideoCapture(0)
    #     cap.set(3, 640)
    #     cap.set(4, 480)
    #     # (screen_w, screen_h) = pdi.size()
    #     mp_hands = mp.solutions.hands
    #     hands = mp_hands.Hands()
    #     mp_draw = mp.solutions.drawing_utils

    #     while True:
    #         _, img = cap.read()
    #         img = cv2.flip(img, 1)
    #         h, w, _ = img.shape
    #         img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #         results = hands.process(img_RGB)

    #         if results.multi_hand_landmarks:
    #             # for hand in results.multi_handedness:
    #             for i, hand_lmks in enumerate(results.multi_hand_landmarks):
    #                 if results.multi_handedness[i].classification[0].label == 'Right':
    #                     curr_hand = self._hand1
    #                 else:
    #                     curr_hand = self._hand2
    #                 tracker = {}
    #                 count = -1
    #                 for id, lm in enumerate(hand_lmks.landmark):
    #                     # print(len(hand_lmks.landmark))
    #                     lm_x, lm_y, lm_z = int(lm.x * w), int(lm.y * h), lm.z
    #                     if id % 4 != 1 and count != -1:
    #                         tracker[count].append((lm_x, lm_y, lm_z))
    #                     elif count == -1:
    #                         curr_hand.set_palm_loc((lm_x, lm_y, lm_z))
    #                         count += 1
    #                     else:
    #                         count += 1
    #                         tracker[count] = [(lm_x, lm_y, lm_z)]
    #                 mp_draw.draw_landmarks(img, hand_lmks, mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2), mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))
    #                 self._set_fingers_loc(tracker, curr_hand)
    #                 # curr_hand.set_palm_loc()
    #             # try:
    #             #     self._mouse_actions.check_match(self._hand1.get_open())
    #             # except:
    #             #     pass
    #             # try:
    #             #     self._keyboard_actions.check_match(self._hand2.get_open())
    #             # except:
    #             #     pass
    #             # print(curr_hand)
    #             try:
    #                 # print(self._hand1.get_open())
    #                 self._signs.get_pos(self._hand1.get_open())
    #             except:
    #                 pass


    
    def _set_fingers_loc(self, tracker, curr_hand):
        for i, finger in enumerate(curr_hand.get_fingers()):
            finger.set_pos(tracker[i + 1][0], tracker[i + 1][1], tracker[i + 1][2], tracker[i + 1][3])