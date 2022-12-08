
class Hand:
    """
        The Hand class:

        This class holds information about which hand it is, which fingers it has,
        the location of the point at the base of the palm, and which fingers are open
        on the hand.
    """
    def __init__(self, hand, fingers, palm):
    # The initialization function, creates the variables that store the hand name, which fingers it has, and the palm location
        self._hand = hand
        self._fingers = fingers
        self._palm = palm
    
    def get_name(self):
    # Returns the name of the hand
        return self._hand
    
    def set_palm_loc(self, loc):
    # Updates the location of the point at the base of the palm
        self._palm = loc
    
    def get_palm_loc(self):
    # Returns the location of the point at the base of the palm
        return self._palm
    
    def get_fingers(self):
    # Returns all finger objects that are in this hand
        return self._fingers
    
    def get_open(self):
    # Returns a list of which fingers are opened
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