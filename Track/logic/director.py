import cv2
import mediapipe as mp
import time
import numpy as np
import pyautogui
import pydirectinput as pdi
import autoit
from logic.handle_action import Handle_Action
from logic.finger import Finger

class Director:
    def __init__(self):
        self._thumb = Finger('thumb')
        self._pointer = Finger('pointer')
        self._middle = Finger('middle')
        self._ring = Finger('ring')
        self._pinky = Finger('pinky')
        self._fingers = [self._thumb, self._pointer, self._middle, self._ring, self._pinky]
        self._actions = Handle_Action(self._fingers)
    
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
            img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_RGB)

            if results.multi_hand_landmarks:
                curr_hand = []
                for hand in results.multi_handedness:
                    curr_hand.append(hand.classification[0].label)
                for hand_lmks in results.multi_hand_landmarks:
                    tracker = {}
                    count = -1
                    for id, lm in enumerate(hand_lmks.landmark):
                        h, w, _ = img.shape
                        lm_x, lm_y, lm_z = int(lm.x * w), int(lm.y * h), lm.x
                        if id % 4 != 1 and count != -1:
                            tracker[count].append((lm_x, lm_y, lm_z))
                        else:
                            count += 1
                            tracker[count] = [(lm_x, lm_y, lm_z)]
                        # if id == 8:
                        #     print(f'x: {lm_x}, y: {lm_y}')
                    mp_draw.draw_landmarks(img, hand_lmks, mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2), mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))
                self._set_finger_loc(tracker)
                self._actions.check(curr_hand)

            cv2.imshow("Image", img)
            cv2.waitKey(1)
    
    def _set_finger_loc(self, tracker):
        for i, finger in enumerate(self._fingers):
            finger.set_pos(tracker[i + 1][0], tracker[i + 1][1], tracker[i + 1][2], tracker[i + 1][3])