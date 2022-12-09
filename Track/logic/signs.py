import pyautogui
import time


class Signs:
    """
        The Signs class:

        This class checks if certain finger positions match that of letters in the ASL alphabet.
        If there is a match, then the key corresponding to that letter will be pressed.
    """
    def __init__(self, fingers, palm):
    # The initialization function, sets up variables that need to be used to get information from each finger, and if an action can be done
        self._fingers = fingers
        self._thumb = fingers[0]
        self._pointer = fingers[1]
        self._middle = fingers[2]
        self._ring = fingers[3]
        self._pinky = fingers[4]
        self._palm = palm


    def _get_pos(self):
    # Returns the positions on each finger
        thumb = self._thumb.get_pos()
        pointer = self._pointer.get_pos()
        middle = self._middle.get_pos()
        ring = self._ring.get_pos()
        pinky = self._pinky.get_pos()

        return (thumb, pointer, middle, ring, pinky)

    def check_letter(self, open):
    # Checks if a letter can be pressed based on finger point locations. If it can, then it calls the function to press that key
        (thumb, pointer, middle, ring, pinky) = self._get_pos()
        if open == [] and thumb[3][0] < pointer[1][0] and thumb[3][1] < thumb[2][1] and thumb[3][1] < pointer[2][1]:
            self._press('a')
        elif open == ['pointer', 'middle', 'ring', 'pinky'] and thumb[3][0] > middle[0][0] and thumb[3][1] > middle[1][1]:
            self._press('b')
        elif thumb[3][1] > pointer[3][1] and pointer[2][1] > pointer[1][1] and thumb[3][2] < pinky[3][2] and thumb[3][0] < middle[3][0] and middle[3][1] > middle[2][1] and pointer[3][1] > pointer[2][1]:
            self._press('c')
        elif open == ['pointer'] and thumb[3][0] > pointer[0][0]:
            self._press('d')
        elif open == [] and pointer[1][1] < pointer[0][1] and thumb[3][0] > pointer[0][0] and thumb[3][1] > middle[3][1]:
            self._press('e')
        elif open == ['middle', 'ring', 'pinky'] and thumb[3][1] < thumb[2][1]:
            self._press('f')
        elif open == [] and pointer[3][1] < ring[0][1] and pointer[2][0] < middle[3][0] and thumb[0][1] < middle[1][1]:
            self._press('g')
        elif open == [] and thumb[3][0] > middle[2][0] and pointer[3][1] < ring[0][1] and pointer[2][0] > middle[3][0] and middle[3][0] < middle[2][0]:
            self._press('h')
        elif open == ['pinky'] and pinky[3][0] > middle[3][0]:
            self._press('i')
        elif 'pinky' in open and pinky[3][0] < pointer[3][0]:
            self._press('j')
        elif open == ['pointer', 'middle'] and thumb[3][0] > pointer[1][0] and pointer[3][0] < middle[3][0] and thumb[3][0] < middle[1][0] and thumb[3][1] < pointer[0][1]:
            self._press('k')
        elif open == ['pointer', 'thumb']:
            self._press('l')
        elif open == [] and thumb[2][2] > ring[2][2] and pointer[1][1] < pointer[0][1] and thumb[3][0] > middle[3][0] and thumb[3][1] < ring[3][1] and thumb[3][1] > ring[1][1]:
            self._press('m')
        elif open == [] and thumb[2][2] > middle[3][2] and pointer[1][1] < pointer[0][1] and thumb[3][0] > middle[2][0] and thumb[3][1] < middle[3][1]:
            self._press('n')
        elif 'thumb' in open and len(open) <= 2 and thumb[3][2] > pinky[3][2] and thumb[3][1] > pointer[2][1] and thumb[3][0] < pointer[2][0] and thumb[3][2] > pointer[3][2] and pointer[3][1] > pointer[2][1]:
            self._press('o')
        elif 'thumb' not in open and 'pointer' not in open and 'middle' not in open and pointer[1][1] > pointer[0][1] and pointer[3][1] > pointer[2][1] and middle[3][1] > middle[2][1] and thumb[3][0] > pointer[3][0]:
            self._press('p')
        elif 'pointer' not in open and thumb[3][0] < middle[2][0] and pointer[3][1] > pointer[2][1] and thumb[3][1] > thumb[2][1]:
            self._press('q')
        elif open == ['pointer', 'middle'] and pointer[3][2] < middle[2][2]and pointer[3][0] > middle[3][0]:
            self._press('r')
        elif open == [] and thumb[3][1] < thumb[1][1] and thumb[3][0] > middle[3][0] and pointer[1][1] < pointer[0][1]:
            self._press('s')
        elif open == [] and thumb[3][0] > pointer[3][0] and thumb[2][2] > pointer[2][2] and thumb[3][0] < middle[3][0]:
            self._press('t')
        elif open == ['pointer', 'middle'] and thumb[3][0] > middle[3][0]:
            self._press('u')
        elif open == ['pointer', 'middle'] and thumb[3][0] < middle[3][0] and thumb[3][0] > pointer[3][0]:
            self._press('v')
        elif open == ['pointer', 'middle', 'ring']:
            self._press('w')
        elif 'pointer' not in open and 'middle' not in open and 'ring' not in open and pointer[3][1] < pointer[0][1] and thumb[3][2] < pointer[0][2]:
            self._press('x')
        elif open == ['pinky', 'thumb']:
            self._press('y')
        elif 'thumb' not in open and pointer[3][2] < pointer[2][2]:
            self._press('z')
        elif open == ['pointer', 'pinky', 'thumb']:
            self._press('backspace')
            
        time.sleep(.8)

    def _press(self, key):
    # Presses the given key
        pyautogui.press(key)