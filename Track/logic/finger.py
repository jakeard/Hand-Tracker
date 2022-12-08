
class Finger():
    """
        The Finger class:

        This class creates the finger objects that can be updated with new locations for each iteration
    """
    def __init__(self, name, point1=0, point2=0, point3=0, point4=0):
    # The initialization function, creates the variables that store the points, and the name of the finger
        self._name = name
        self._base = point1
        self._low = point2
        self._mid = point3
        self._top = point4
    
    def set_pos(self, p1, p2, p3, p4):
    # Used to update the location of the points on the fingers
        self._base = p1
        self._low = p2
        self._mid = p3
        self._top = p4

    def get_pos(self):
    # Returns all points' coordinates for the finger
        return (self._base, self._low, self._mid, self._top)
    
    def get_specific_pos(self, pos):
    # Returns the specified point's coordinates for the finger
        if pos == 'top':
            point = self._top
        elif pos == 'low':
            point = self._low
        elif pos == 'base':
            point = self._base
        elif pos == 'mid':
            point = self._mid
        return point
    
    def get_name(self):
    # Returns the name of the finger
        return self._name