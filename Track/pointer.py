import cv2
import mediapipe as mp
import time
from finger import Finger

class Pointer(Finger):
    def __init__(self, p1, p2, p3, p4):
        super().__init__('pointer', p1, p2, p3, p4)
