import cv2
import mediapipe as mp
import time
from logic.handle_action import Handle_Action
from logic.finger import Finger

class Director:
    def __init__(self):
        self.thumb = Finger('thumb')
        self.pointer = Finger('pointer')
        self.middle = Finger('middle')
        self.ring = Finger('ring')
        self.pinky = Finger('pinky')
        self.fingers = [self.thumb, self.pointer, self.middle, self.ring, self.pinky]
    
    def run(self):
        cap = cv2.VideoCapture(0)

        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        mp_draw = mp.solutions.drawing_utils

        while True:
            _, img = cap.read()
            img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_RGB)

            if results.multi_hand_landmarks:
                for hand_lmks in results.multi_hand_landmarks:
                    tracker = {}
                    count = -1
                    for id, lm in enumerate(hand_lmks.landmark):
                        if id % 4 != 1 and count != -1:
                            tracker[count].append((lm.x, lm.y, lm.z))
                        else:
                            count += 1
                            tracker[count] = [(lm.x, lm.y, lm.z)]
                        # if count == 2 and id == 8: 
                        # and tracker[count][3][1] > tracker[count][1][1]:
                            # print(lm.z)
                    mp_draw.draw_landmarks(img, hand_lmks, mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2), mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))
                self.set_finger_loc(tracker)
                Handle_Action(self.fingers)
                # print(tracker[1][3])

            cv2.imshow("Image", img)
            cv2.waitKey(1)
    
    def set_finger_loc(self, tracker):
        for i, finger in enumerate(self.fingers):
            finger.set_pos(tracker[i + 1][0], tracker[i + 1][1], tracker[i + 1][2], tracker[i + 1][3])
            
    
    # def record_finger_pos(self, tracker):
