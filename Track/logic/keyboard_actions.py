import autoit
from pynput.keyboard import Key, Controller
import time

class Keyboard_Actions:
    def __init__(self, fingers):
        self._fingers = fingers
        self._thumb = fingers[0]
        self._pointer = fingers[1]
        self._middle = fingers[2]
        self._ring = fingers[3]
        self._pinky = fingers[4]
        # self._prev_pros = (0, 0)
        self._pressed = 'z'
        # self._press = None
        # self._currently_pressed = None
        self._keyboard = Controller()
    
    def check_match(self, open):
        press = None
        if open == ['pointer']:
            press = 'w'
            # self._keyboard.release(self._pressed)
            # self._keyboard.press('w')
            # self._pressed = 'w'
            # self._keyboard.release('w')
            # autoit.send('W')
        elif open == ['pointer', 'middle']:
            press = 'a'
            # self._press_key('a')
            # self._keyboard.release(self._pressed)
            # self._keyboard.press('a')
            # self._keyboard.press('w')
            # self._pressed = 'a'
            # autoit.send('A')
        elif open == ['pointer', 'middle', 'ring']:
            press = 's'
            # self._press_key('s')
            # self._keyboard.press('w')
            # self._keyboard.release(self._pressed)
            # self._keyboard.press('s')
            # self._pressed = 's'
            # autoit.send('S')
        elif open == ['pointer', 'middle', 'ring', 'pinky']:
            # print('AHHHHHHHHHHHHHHHHHHHHHHHHH')
            press = 'd'
        # else:
            # press = None
            # self._press_key('d')
            # self._keyboard.release(self._pressed)
            # self._keyboard.press('d')
            # self._pressed = 'd'
            # autoit.send('D')
        # else:
            # self._keyboard.release(self._pressed)
        self._press_key(press)
        # autoit.send()
        # self._check_w(open)
    
    # def _is_pressed(self, key):
    #     if self._pressed != key:
    #         return True
    #     return False

    def _press_key(self, key):
        # self._keyboard.release(self._pressed)
        # if key is not None:
        if key != self._pressed:
            self._keyboard.release(key)
        if key is not None:
            self._keyboard.press(key)
        self._pressed = key
    # def _check_w(self, open):
