from macpath import curdir

class MagicSquare():
       
    """Notation:
    0,0 0,1 0,2
    1,0 1,1 1,2
    2,0 2,1 2,2
    
    http://en.wikipedia.org/wiki/Magic_square
    http://en.wikipedia.org/wiki/Pandiagonal_magic_square
    """
       
    def printSquare(self, square):
        """print the square to the screen
        Return None
        """
        for line in square:
            print(line)
        return None
    
    def generateOdd(self, dimension, initial=None, increment=None):
        """generate odd dimension square
        return square obj
        """
        if dimension % 2 == 0:
            raise ValueError("dimension must be an odd positive integer")
        
        if not initial:
            initial = 1
        if not increment:
            increment = 1
            
        #Create empty square
        square = []
        for _ in xrange(dimension):
            line = []
            for _ in xrange(dimension):
                line.append(None)
            square.append(line)
            
        #Setup algorithm
        y = 0
        x = dimension/2
        cur = initial
                
        for _ in xrange(dimension**2):
            square[y][x] = cur
            cur += increment
            
            #if top right corner
            if (y == 0) and (x == dimension - 1):
                x = x
                y = 1
            #if top edge
            elif y == 0:
                x += 1
                y = dimension - 1
            #if right edge
            elif x == dimension - 1:
                x = 0
                y -= 1
            #if number already there
            elif square[y-1][x+1]:
                x = x
                y += 1
            else:
                x += 1
                y -= 1
            
        return square
    
    def testSemiMagic(self, square):
        """Test if a square is Semi-Magic (lines but NOT diagonals)
        Return Bool
        """
        s = sum(square[0])
        #rows
        for row in square:
            if sum(row) != s:
                return False        
        #cols
        for x in xrange(len(square) - 1):
            p = 0
            for row in square:
                p += row[x]
            if p != s:
                return False
        #diagonals
        #duplicates
        
        return True
    
    def testMagic(self, square):
        """Test if a square is Magic (lines AND diagonals)
        Return bool"""
        s = sum(square[0])
        #rows
        for row in square:
            if sum(row) != s:
                return False        
        #cols
        for x in xrange(len(square) - 1):
            p = 0
            for row in square:
                p += row[x]
            if p != s:
                return False
        #diagonals
        #duplicates
        
        return True