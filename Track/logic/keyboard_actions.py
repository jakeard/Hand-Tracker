import pyautogui
import pydirectinput as pdi

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
        self._pressed = None
    
    def check_match(self, open):
    # Compares open fingers to what is needed to do a specific action
        press = None
        if open == ['pointer']:
            self._press_key('w')
        elif open == ['pointer', 'middle']:
            self._press_key('a')
        elif open == ['pointer', 'middle', 'ring']:
            self._press_key('s')
        elif open == ['pointer', 'middle', 'ring', 'pinky']:
            self._press_key('d')

    def _press_key(self, key):
    # Controls key presses and releases
        if key and self._pressed != key:
            pdi.keyUp(self._pressed)
            pdi.keyDown(key)
            self._pressed = key
        elif not key:
            pdi.keyUp(self._pressed)