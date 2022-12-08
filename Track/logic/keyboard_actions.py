import pyautogui
import pydirectinput as pdi
import time

class Keyboard_Actions:
    """
        The Keyboard_Actions class:

        This class looks at the points on the left hand and compares them to an action that 
        has specific point location requirements. If it is a match, then the action is
        done. If not, then the action is passed.
    """
    def __init__(self, fingers):
    # The initialization function, sets up variables that need to be used to get information from each finger
        self._fingers = fingers
        self._thumb = fingers[0]
        self._pointer = fingers[1]
        self._middle = fingers[2]
        self._ring = fingers[3]
        self._pinky = fingers[4]
        # self._prev_pros = (0, 0)
        self._pressed = None
        # self._press = None
        # self._currently_pressed = None
        # self._keyboard = Controller()
    
    def check_match(self, open):
    # Compares open fingers to what is needed to do a specific action
        press = None
        if open == ['pointer']:
            self._press_key('w')
            # press = 'w'
            # self._keyboard.release(self._pressed)
            # self._keyboard.press('w')
            # self._pressed = 'w'
            # self._keyboard.release('w')
            # autoit.send('W')
        elif open == ['pointer', 'middle']:
            self._press_key('a')
            # press = 'a'
            # self._press_key('a')
            # self._keyboard.release(self._pressed)
            # self._keyboard.press('a')
            # self._keyboard.press('w')
            # self._pressed = 'a'
            # autoit.send('A')
        elif open == ['pointer', 'middle', 'ring']:
            self._press_key('s')
            # press = 's'
            # self._press_key('s')
            # self._keyboard.press('w')
            # self._keyboard.release(self._pressed)
            # self._keyboard.press('s')
            # self._pressed = 's'
            # autoit.send('S')
        elif open == ['pointer', 'middle', 'ring', 'pinky']:
            # print('AHHHHHHHHHHHHHHHHHHHHHHHHH')
            self._press_key('d')
            # press = 'd'
        # else:
            # press = None
            # self._press_key('d')
            # self._keyboard.release(self._pressed)
            # self._keyboard.press('d')
            # self._pressed = 'd'
            # autoit.send('D')
        # else:
            # self._keyboard.release(self._pressed)
        # autoit.send()
        # self._check_w(open)

    def _press_key(self, key):
    # Controls key presses and releases
        if key and self._pressed != key:
            pdi.keyUp(self._pressed)
            pdi.keyDown(key)
            self._pressed = key
        elif not key:
            pdi.keyUp(self._pressed)