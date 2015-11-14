import random
import statistics
from errors import *

class Square(object):
    def __init__(self, order):
        self.order = order
        self.square = []
        #Create empty square
        """
        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2
        """
        for _ in range(self.order):
            line = []
            for _ in range(self.order):
                line.append(None)
            self.square.append(line)
        
    def printSquare(self):
        """Print the square to the screen for humans
        Return None
        """
        for row in self.square:
            print(row)
        return None

    def populateRandom(self):
        """Populate the self.square with random numbers
        Return None
        """
        for x in range(self.order):
            for y in range(self.order):
                self.square[y][x] = random.randrange(1, self.order**2)
        return None
                
    def importSquare(self, square):
        """Import a square to self.square
        Return True or Raise DimError
        """
        if len(square) != len(self.square):
            raise DimError('Imported square must be same order')
        self.square = square
        return True
        
    def evaluateFitness(self):
        """evaluate the fitness of the candidate
        Return Float
        """
        #all sums into a list
        values = []
        #rows
        for row in self.square:
            values.append(sum(row))
        #cols
        for x in range(self.order):
            p = 0
            for row in self.square:
                p += row[x]
            values.append(p)
        #diagonals
        x1, y1 = 0, 0
        x2, y2 = self.order -1, 0
        d1, d2 = 0, 0
        for _ in range(self.order):
            d1 += self.square[y1][x1]
            d2 += self.square[y2][x2]
            y1 += 1
            x1 += 1
            y2 += 1
            x2 -= 1
        values.append(d1)
        values.append(d2)
        
        print(values)
        
    def generateRowValues(self):
        """Generate values of line totals
        row: Dict of Row totals indexed by left most position
        col: Dict of Column totals indexed by top most position
        dia: Dict of Diagonal  totals indexed by top corner positions
        dis: Tuple of all line and diagonal totals
        
        {'row': {
            (0,0): n,
            (1,0): m },
         'col': {
             (0,0): n,
             (0,1): m },
         'dia': {
             (0,0): n,
             (0,x): m},
         'dis': (m,n,o,p,...)
        }
        
        Return Dict
        """
        rowvalues = {'row': {},
                     'col': {},
                     'dia': {},
                     'dis': ()}
        
        # Rows
        for i in range(self.order):
            rowvalues['row'][(i,0)] = sum(self.square[i])
            
        # Columns
        for i in range(self.order):
            p = 0
            for row in self.square:
                p += row[i]
            rowvalues['col'][(0,i)] = p
        
        # Diagonals
        x1, y1 = 0, 0
        x2, y2 = self.order - 1, 0
        d1, d2 = 0, 0
        for _ in range(self.order):
            d1 += self.square[y1][x1]
            d2 += self.square[y2][x2]
            y1 += 1
            x1 += 1
            y2 += 1
            x2 -= 1
        rowvalues['dia'][(0,0)] = d1
        rowvalues['dia'][(self.order - 1, 0)] = d2
        
        # Distribution
        dis = []
        for v in rowvalues['row'].values():
            dis.append(v)
        for v in rowvalues['col'].values():
            dis.append(v)
        for v in rowvalues['dia'].values():
            dis.append(v)
        rowvalues['dis'] = tuple(dis)
        
        return rowvalues
    
if __name__ == '__main__':
    pass
