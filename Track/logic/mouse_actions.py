import autoit
import numpy as np


class Mouse_Actions:
    """
        The Mouse_Actions class:

        This class looks at the points on the right hand and compares them to an action that 
        has specific point location requirements. If it is a match, then the action is
        done. If not, then the action is passed.
    """
    def __init__(self, fingers):
    # The initialization function, sets up variables that need to be used to get information from each finger, and if an action can be done
        self._fingers = fingers
        self._thumb = fingers[0]
        self._pointer = fingers[1]
        self._middle = fingers[2]
        self._ring = fingers[3]
        self._pinky = fingers[4]
        self._prev_pros = (0, 0)
        self._can_click_left = True
        self._can_click_right = True
    #     self._movable = self._create_allowed_moves()

    # def _create_allowed_moves(self):
    #     moves = [['pointer'], ['pointer', 'thumb'], ['pointer', 'middle']]
    #     return moves
    
    def check_match(self, open):
    # Compares open fingers to what is needed to do a specific action
        if not self._can_click_left or not self._can_click_right:
            self._reset_can_clicks(open)
        self._check_scroll_up(open)
        self._check_scroll_down(open)
        self._check_left_click(open)
        self._check_right_click(open)
        self._check_move_mouse(open)
    
    def _reset_can_clicks(self, open):
    # Resets the can_click variable for left and right click
        if 'thumb' not in open:
            self._can_click_left = True
        if 'middle' not in open:
            self._can_click_right = True
    
    def _check_move_mouse(self, open):
    # Checks if the current open fingers match the requirements to move the mouse
        # if open == ['pointer']:
        # if open in self._movable:
        if open == ['pointer']:
            # print('move')
            self._move()
    
    def _check_left_click(self, open):
    # Checks if the current open fingers match the requirements to left click the mouse
        if open == ['pointer', 'thumb'] and self._can_click_left:
        # if self._open_match(open, 'thumb'):
        # if self._thumb.get_specific_pos('top')[1] > self._pointer.get_specific_pos('mid')[1] and self._can_click:
            self._can_click_left = False
            # print('left click')
            self._click('left')

    def _check_right_click(self, open):
    # Checks if the current open fingers match the requirements to right click the mouse
        if open == ['pointer', 'middle'] and self._can_click_right:
            self._can_click_right = False
            # print('right click')
            self._click('right')
    
    def _check_scroll_up(self, open):
    # Checks if the current open fingers match the requirements to scroll up on the mouse
        if open == ['pointer', 'middle', 'ring']:
            # print('scroll up')
            self._scroll('up')

    def _check_scroll_down(self, open):
    # Checks if the current open fingers match the requirements to scroll down on the mouse
        if open == ['pointer', 'middle', 'ring', 'pinky']:
            # print('scroll down')
            self._scroll('down')

    def _move(self):
    # Moves the mouse to a point corresponding to the top of the pointer finger
        (x, y, z) = self._pointer.get_specific_pos('top')

        x = np.interp(x, (150, 490), (0, 1920))
        y = np.interp(y, (100, 250), (0, 1080))

        curx = round(self._prev_pros[0] + (x - self._prev_pros[0]) / 3)
        cury = round(self._prev_pros[1] + (y - self._prev_pros[1]) / 3)

        self._prev_pros = (curx, cury)

        autoit.mouse_move(curx, cury, 0)
    
    def _click(self, side):
    # Clicks the mouse (right or left)
        autoit.mouse_click(side)

    def _scroll(self, direction):
    # Scrolls the mouse (up or down)
        autoit.mouse_wheel(direction, 1)