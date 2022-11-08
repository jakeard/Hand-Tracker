import autoit

class Keyboard_Actions:
    def __init__(self, fingers):
        self._fingers = fingers
        self._thumb = fingers[0]
        self._pointer = fingers[1]
        self._middle = fingers[2]
        self._ring = fingers[3]
        self._pinky = fingers[4]
        self._prev_pros = (0, 0)
    
    def check_match(self, open):
        if open == ['pointer']:
            autoit.send('W')
        if open == ['pointer', 'middle']:
            autoit.send('A')
        if open == ['pointer', 'middle', 'ring']:
            autoit.send('S')
        if open == ['pointer', 'middle', 'ring', 'pinky']:
            autoit.send('D')
        # self._check_w(open)

    # def _check_w(self, open):
