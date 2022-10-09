import cv2
import mediapipe as mp
import time

class Finger:
    def __init__(self, identify, point1, point2, point3, point4):
        self.name = identify
        self._base = point1
        self._low = point2
        self._mid = point3
        self._top = point4
    
    def set_pos(self, p1, p2, p3, p4):
        self._base = p1
        self._low = p2
        self._mid = p3
        self._top = p4

    def get_pos(self):
        return (self.base, self.low, self.mid, self.top)