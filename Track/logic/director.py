import cv2
import mediapipe as mp
from logic.finger import Finger
from logic.hand import Hand
from logic.mouse_actions import Mouse_Actions
from logic.keyboard_actions import Keyboard_Actions
from logic.signs import Signs

class Director:
    """
        The Director class:

        This class is the main loop of the program and handles creating the fingers and hands objects,
        connecting to the camera, and using MediaPipe to get point coordinates and update the finger objects
        with those points. 
    """
    def __init__(self, todo): 
    # The initialization function, creates the hand objects and sets up other classes that need to be used
        self._hand1 = Hand('Right', self._create_fingers(), 0)
        self._hand2 = Hand('Left', self._create_fingers(), 0)
        self._mouse_actions = Mouse_Actions(self._hand1.get_fingers())
        self._keyboard_actions = Keyboard_Actions(self._hand2.get_fingers())
        self._signs = Signs(self._hand1.get_fingers(), self._hand1.get_palm_loc())
        if todo == 'mouse': # sets if ASL or mouse and WASD
            self._todo = self._mouse_and_key
        else:
            self._todo = self._asl
    
    def _create_fingers(self):
    # Creates the finger objects to be put into a hand object
        return [Finger('thumb'), Finger('pointer'), Finger('middle'), Finger('ring'), Finger('pinky')]
    
    def run(self):
    # Main loop, uses camera and MediaPipe to get hand point locations, shows the camera's view, and calls the correct thing to do with the information
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        mp_draw = mp.solutions.drawing_utils

        while True:
            _, img = cap.read()
            img = cv2.flip(img, 1)
            h, w, _ = img.shape
            img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_RGB)

            if results.multi_hand_landmarks: # if a hand is detected do the following
                for i, hand_lmks in enumerate(results.multi_hand_landmarks):
                    if results.multi_handedness[i].classification[0].label == 'Right':
                        curr_hand = self._hand1
                    else:
                        curr_hand = self._hand2
                    tracker = {}
                    count = -1
                    for id, lm in enumerate(hand_lmks.landmark):
                        lm_x, lm_y, lm_z = int(lm.x * w), int(lm.y * h), lm.z
                        if id % 4 != 1 and count != -1:
                            tracker[count].append((lm_x, lm_y, lm_z))
                        elif count == -1:
                            curr_hand.set_palm_loc((lm_x, lm_y, lm_z)) # The palm has 1 point, this call updates that point
                            count += 1
                        else:
                            count += 1
                            tracker[count] = [(lm_x, lm_y, lm_z)]
                    mp_draw.draw_landmarks(img, hand_lmks, mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2), mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)) # draws the lines and dots on visible hands
                    self._set_fingers_loc(tracker, curr_hand)
                self._todo() # call the class to do the actions
                
            cv2.imshow("Image", img) # show the image
            cv2.waitKey(1)

    def _mouse_and_key(self):
    # Checks if hand positions match to an action (moving mouse and/or pressing WASD)
        try:
            self._mouse_actions.check_match(self._hand1.get_open())
        except:
            pass
        try:
            self._keyboard_actions.check_match(self._hand2.get_open())
        except:
            pass
    
    def _asl(self):
    # Checks if hand positions match to an action (sign language letters)
        try:
            # print(self._hand1.get_open())
            self._signs.check_letter(self._hand1.get_open())
        except:
            pass
    
    def _set_fingers_loc(self, tracker, curr_hand):
    # Each finger has 4 points, updates each fingers 4 points with the coordinates from run()
        for i, finger in enumerate(curr_hand.get_fingers()):
            finger.set_pos(tracker[i + 1][0], tracker[i + 1][1], tracker[i + 1][2], tracker[i + 1][3])