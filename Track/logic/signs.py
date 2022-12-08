import pyautogui
# import pydirectinput as pdi


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
        print(open)
        if open == [] and thumb[3][0] < pointer[1][0] and thumb[3][1] < thumb[2][1] and thumb[3][1] < pointer[2][1]:
            print('a')
            # self._press('a')
        elif open == ['pointer', 'middle', 'ring', 'pinky'] and thumb[3][0] > middle[0][0] and thumb[3][1] > middle[1][1]:
           print('b') 
            # self._press('b')
        # else:
        # elif len(open) <= 2 and thumb[3][2] > pinky[3][2] and thumb[3][1] > pointer[2][1] and thumb[3][0] < pointer[2][0] and thumb[3][2] > pointer[3][2] and pointer[3][1] > pointer[2][1]:
        elif thumb[3][1] > pointer[3][1] and thumb[3][0] < middle[3][0] and middle[3][1] > middle[2][1] and pointer[3][1] > pointer[2][1]:
        # elif 'thumb' in open and len(open) <= 2 and thumb[3][2] > pinky[3][2] and thumb[3][1] > pointer[2][1] and thumb[3][0] < pointer[2][0] and thumb[3][2] > pointer[3][2] and pointer[3][1] > pointer[2][1]:
            # self._press('c')
            print('c')
        elif open == ['pointer'] and thumb[3][0] > pointer[0][0]:
            # self._press('d')
            print('d')
        elif open == [] and thumb[3][0] > pointer[0][0] and thumb[3][1] > middle[3][1]:
            # self._press('e')
            print('e')
        elif open == ['middle', 'ring', 'pinky']:
            print('f')
        elif open == [] and pointer[3][1] < ring[0][1] and pointer[2][0] < middle[3][0]:
            print('g')
        elif open == [] and pointer[3][1] < ring[0][1] and pointer[2][0] > middle[3][0]:
            print('h')
        elif open == ['pinky'] and pinky[3][0] > middle[3][0]:
            print('i')
        elif open == ['pinky'] and pinky[3][0] < middle[2][0]:
        # elif open == [] and pinky[3][0] < ring[2][0] and pinky[3][1] > middle[2][1]:
            print('j')
        elif open == ['pointer', 'middle'] and thumb[3][0] > pointer[1][0]:
            print('k')
        elif open == ['pointer', 'thumb']:
            print('l')
        elif open == [] and thumb[3][0] > middle[3][0] and thumb[3][1] < ring[3][1] and thumb[3][1] > ring[1][1]:
            print('m')
        elif open == [] and thumb[3][0] > pointer[3][0] and thumb[3][1] < middle[3][1]:
            print('n')
    

    def _press(self, key):
    # Presses the given key
        pyautogui.press(key)