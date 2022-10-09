import cv2
import mediapipe as mp
import time
from finger import Finger

class Director:
    def __init__(self):
        self.thumb = Finger()
        self.pointer = Finger()
        self.middle = Finger()
        self.ring = Finger()
        self.pinky = Finger()
        self.fingers = [self.thumb, self.pointer, self.middle, self.ring, self.pinky]
    
    def run(self):
        cap = cv2.VideoCapture(0)

        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        mp_draw = mp.solutions.drawing_utils

        # ind = 0
        while True:
            _, img = cap.read()
            img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_RGB)

            if results.multi_hand_landmarks:
                for hand_lmks in results.multi_hand_landmarks:
                    tracker = {}
                    count = -1
                    for id, lm in enumerate(hand_lmks.landmark):
                        if id % 4 == 1 or count == -1:
                            count += 1
                            tracker[count] = [(lm.x, lm.y, lm.z)]
                            continue
                        tracker[count].append((lm.x, lm.y, lm.z))
                    self.set_finger_loc(tracker)
                    mp_draw.draw_landmarks(img, hand_lmks, mp_hands.HAND_CONNECTIONS)
            cv2.imshow("Image", img)
            cv2.waitKey(1)
            # if ind % 10 == 0:
                # print(self.pointer.get_pos())
            # ind += 1
    
    def set_finger_loc(self, tracker):
        for i, finger in enumerate(self.fingers):
            current = i + 1
            finger.set_pos(tracker[current][0], tracker[current][1], tracker[current][2], tracker[current][3])