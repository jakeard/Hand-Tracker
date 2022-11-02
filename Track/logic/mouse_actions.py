import autoit
import numpy as np


class Mouse_Actions:
    def __init__(self, fingers):
        self.fingers = fingers
        self.thumb = fingers[0]
        self.pointer = fingers[1]
        self.middle = fingers[2]
        self.ring = fingers[3]
        self.pinky = fingers[4]


    def move_mouse(self):
        (x, y) = self.pointer.get_specific_pos('top')
        x = round(np.interp(x, (150, 490), (0, 1920)))
        y = round(np.interp(y, (100, 380), (0, 1920)))
        # print(f"x: {x}, y: {y}\n")
        # print(x, y)
        # curx = round(self.prev_pos[0] + (x - self.prev_pos[0]) / 5)
        # cury = round(self.prev_pos[1] + (y - self.prev_pos[1]) / 5)
        # print(curx, cury)
        # diff_x = self.prev_pos[0] - x
        # diff_y = self.prev_pos[1] - y
        # first_x = x
        # first_y = y
        # if self.prev_pos[0] > x:
        #     first_x = x + 1
        # elif self.prev_pos[0] < x:
        #     first_x = x - 1

        # if self.prev_pos[1] > y:
        #     first_y = y + 1
        # elif self.prev_pos[1] < y:
        #     first_y = y - 1

        
        
        # autoit.mouse_move(x - 2, y - 2, 0)
        # autoit.mouse_move(x - 1, y - 1, 0)
        # autoit.mouse_move(first_x, first_y, 0)
        autoit.mouse_move(x, y, 0)
        # autoit.mouse_move(curx, cury, 0)
        # self.prev_pos = (x, y)
        # pdi.moveTo(x, y)