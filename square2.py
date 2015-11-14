import numpy as np

class Square2(list):
    def __init__(self, order, values=None):
        """A square object
        
        
        @param order: Integer - The order of the square
        @rtype: List
        @summary: The square is a list of lists
        The positions in the square attribute are indexed using tuples i.e.
        [ [(0,0), (0,1), (0,2)],
          [(1,0), (1,1), (1,2)],
          [(2,0), (2,1), (2,2)] ]
        """
        list.__init__(self)
        self.order = order
        if values:
            self.load(values)
        
    def _hash_(self):
        """Create a hash of the square
        
        @rtype: hash
        @summary: the hash of the square is the same when the square is simply
            rotated
        """
        # find smallest value in a corner
        mincorner = min([self[0][0], self[0][-1], self[-1][0], self[-1][-1]])
        # rotate until smallest corner is top left, then take hash
        for _ in range(4):
            if self[0][0] == mincorner:
                hash_value =  hash(tuple([item for sublist in self for item in sublist]))
            self.rotate()
        
        return hash_value
       
    def load(self, values):
        """Load given values into this object
        
        @param values: List
        @requires: order of square must match self
        @rtype: None
        """
        if len(values) != self.order:
            raise Exception("order of square must match self")
        self.clear()
        self.extend(values)
        
    def rotate(self):
        """Rotate self by 90 degrees in the counter-clockwise direction.
        
        @rtype: List
        """
        self.load(list(zip(*self[::-1])))
        return self
        
