
class Hand:
    def __init__(self, hand, fingers):
        self._hand = hand
        self._fingers = fingers
    
    def get_name(self):
        return self._hand
    
    def get_fingers(self):
        return self._fingers
    
    def get_open(self):
        open = [x.get_name() for x in self._fingers if x.get_specific_pos('top')[1] < x.get_specific_pos('mid')[1] and x.get_name() != 'thumb']
        if self._hand == 'Right':
            if self._fingers[0].get_specific_pos('top')[0] <= self._fingers[1].get_specific_pos('base')[0] - 50:
                open.append('thumb')
        else:
            if self._fingers[0].get_specific_pos('top')[0] >= self._fingers[1].get_specific_pos('base')[0] + 50:
                open.append('thumb')

        return open