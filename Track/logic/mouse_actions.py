import autoit
import numpy as np


class Mouse_Actions:
    def __init__(self, fingers):
        self._fingers = fingers
        self._thumb = fingers[0]
        self._pointer = fingers[1]
        self._middle = fingers[2]
        self._ring = fingers[3]
        self._pinky = fingers[4]
        self._prev_pros = (0, 0)
        self._can_click_left = True
        self._can_click_right = True
        self._movable = self._create_allowed_moves()

    def _create_allowed_moves(self):
        moves = [['pointer'], ['pointer', 'thumb'], ['pointer', 'middle']]
        return moves
    
    def check_match(self, open):
        if not self._can_click_left or not self._can_click_right:
            self._reset_can_clicks(open)
        self._check_move_mouse(open)
        self._check_left_click(open)
        self._check_right_click(open)
        # self._check_scroll_up(open)
        # self._check_scroll_down(open)
    
    def _reset_can_clicks(self, open):
        if 'thumb' not in open:
            self._can_click_left = True
        if 'middle' not in open:
            self._can_click_right = True
    
    def _check_move_mouse(self, open):
        # if open == ['pointer']:
        # if open in self._movable:
        if open == ['pointer']:
            # print('move')
            self._move()
    
    def _check_left_click(self, open):
        if open == ['pointer', 'thumb'] and self._can_click_left:
        # if self._open_match(open, 'thumb'):
        # if self._thumb.get_specific_pos('top')[1] > self._pointer.get_specific_pos('mid')[1] and self._can_click:
            self._can_click_left = False
            # print('left click')
            self._click('left')

    def _check_right_click(self, open):
        if open == ['pointer', 'middle'] and self._can_click_right:
            self._can_click_right = False
            # print('right click')
            self._click('right')
    
    def _check_scroll_up(self, open):
        if open == ['pointer', 'ring']:
            pass

    def _check_scroll_down(self, open):
        if open == ['pointer', 'ring']:
            pass

    def _move(self):
        (x, y, z) = self._pointer.get_specific_pos('top')

        x = np.interp(x, (150, 490), (0, 1920))
        y = np.interp(y, (100, 250), (0, 1080))

        curx = round(self._prev_pros[0] + (x - self._prev_pros[0]) / 2)
        cury = round(self._prev_pros[1] + (y - self._prev_pros[1]) / 2)

        self._prev_pros = (curx, cury)

        autoit.mouse_move(curx, cury, 0)
    
    def _click(self, side):
        autoit.mouse_click(side)

    def _scroll(self, direction):
        autoit.mouse_wheel(direction, 1)