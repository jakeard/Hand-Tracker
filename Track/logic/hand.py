
class Hand:
    def __init__(self, hand, fingers, palm):
        self._hand = hand
        self._fingers = fingers
        self._palm = palm
    
    def get_name(self):
        return self._hand
    
    def set_palm_loc(self, loc):
        self._palm = loc
    
    def get_palm_loc(self):
        return self._palm
    
    def get_fingers(self):
        return self._fingers
    
    def get_open(self):
        if self._palm[1] > self._fingers[4].get_specific_pos('base')[1]:
            open = [x.get_name() for x in self._fingers if x.get_specific_pos('top')[1] < x.get_specific_pos('mid')[1] and x.get_name() != 'thumb']
            if self._hand == 'Right':
                if self._fingers[0].get_specific_pos('top')[0] <= self._fingers[1].get_specific_pos('base')[0] - 50:
                    open.append('thumb')
            else:
                if self._fingers[0].get_specific_pos('top')[0] >= self._fingers[1].get_specific_pos('base')[0] + 50:
                    open.append('thumb')
        else:
            open = []

        return open