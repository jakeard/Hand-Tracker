import cv2
import mediapipe as mp
import time
from finger import Finger

class Thumb(Finger):
    def __init__(self, p1, p2, p3, p4):
        super().__init__('thumb', p1, p2, p3, p4)
    
    def set_pos(self, p1, p2, p3, p4):
        self.top = p4
        self.mid = p3
        self.low = p2
        self.base = p1