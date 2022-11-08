
class Finger():
    def __init__(self, name, point1=0, point2=0, point3=0, point4=0):
        self._name = name
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
        return (self._base, self._low, self._mid, self._top)
    
    def get_specific_pos(self, pos):
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
        return self._name