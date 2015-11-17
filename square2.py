import numpy as np
import random
import math
from collections import namedtuple

class Square2(list):
    def __init__(self, order, values=None):
        """A square object
        
        @param order: Integer - The order of the square
        @param values: Load given values into this object
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
        
        @rtype: Int
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
        
        @param values: List of lists
        @requires: order of square must match self
        @note: Order of values is compatible with loadFlat().
            Here the values are already in lists
        @rtype: None
        """
        assert len(values) == self.order
        
        self.clear()
        self.extend(values)
        return None
        
    def loadFlat(self, values):
        """Load given flat list of values into this object
        
        @param values: list of values
        @requires: len(values) == self.order**2
        @note: Order of values is compatible with load()
        @rtype: None
        """
        assert len(values) == self.order**2
        
        self.clear()
        values.reverse()
        
        for x in range(self.order):
            sublist = []
            for y in range(self.order):
                sublist.append(values.pop())
            self.append(sublist)
        return None
        
    def rotate(self):
        """Rotate self in place by 90 degrees in the counter-clockwise direction.
        
        @rtype: None
        """
        self.load(list(zip(*self[::-1])))
        return None
        
    def populateRandom(self):
        """Populate self with random numbers
        
        @note: This method is an ideal place to expand on later, trying out the effectivness
        of square generation starting with different distributions of random 
        numbers
        
        @rtype: None
        """
        self.loadFlat(random.sample(range(int(math.ceil(self.order**math.e))), self.order**2))
        return None
    
    def getTotals(self):
        """Get the totals of the rows, cols and diagonals
        
        @requires: self.isEmpty() is False
        @rtype: namedtuple
        """
        assert self.isEmpty() is False
        
        Totals = namedtuple("Totals", ["row", "col", "dia"])
        
        row = []
        for i in range(self.order):
            row.append(sum(self[i]))
        row = tuple(row)
        
        col = []
        for i in range(self.order):
            col.append(sum([c[i] for c in self]))
        col = tuple(col)
        
        dia_right = []
        j = 0
        for i in range(self.order):
            dia_right.append(self[i][j])
            j += 1
        dia_left = []
        j = self.order - 1
        for i in range(self.order):
            dia_left.append(self[i][j])
            j -= 1
        dia = (sum(dia_right), sum(dia_left))
        
        return Totals(row, col, dia)
        
            
    def isEmpty(self):
        """Query if self has values loaded
        
        @rtype: bool
        """
        if self == []:
            return True
        else:
            return False
        