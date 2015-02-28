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
        for _ in range(dimension):
            line = []
            for _ in range(dimension):
                line.append(None)
            square.append(line)
            
        #Setup algorithm
        y = 0
        x = dimension//2
        cur = initial
                
        for _ in range(dimension**2):
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
        """Test if a square is Semi-Magic
        (lines equal, at least one diagonal NOT)
        Return Bool
        """
        
        values = []
        #rows
        for row in square:
            values.append(sum(row))
        #cols
        for x in range(len(square)):
            p = 0
            for row in square:
                p += row[x]
            values.append(p)    
            
        # All rows and cols sums equal
        if len(set(values)) != 1:
            return False
        
        #diagonals
        x1, y1 = 0, 0
        x2, y2 = len(square) -1, 0
        d1, d2 = 0, 0
        for _ in range(len(square)):
            d1 += square[y1][x1]
            d2 += square[y2][x2]
            y1 += 1
            x1 += 1
            y2 += 1
            x2 -= 1
            
        if (d1 in values) and (d2 in values):
            return False
        
        #no duplicates
        l = [number for row in square for number in row]
        if len(l) != len(set(l)):
            return False
        
        return True
    
    def testMagic(self, square):
        """Test if a square is Magic
        (lines AND diagonals equal)
        Return bool"""
        
        values = []
        #rows
        for row in square:
            values.append(sum(row))
        #cols
        for x in range(len(square)):
            p = 0
            for row in square:
                p += row[x]
            values.append(p)    
        #diagonals
        x1, y1 = 0, 0
        x2, y2 = len(square) -1, 0
        d1, d2 = 0, 0
        for _ in range(len(square)):
            d1 += square[y1][x1]
            d2 += square[y2][x2]
            y1 += 1
            x1 += 1
            y2 += 1
            x2 -= 1
        values.append(d1)
        values.append(d2)
        
        # All rows, cols and diagonals sums equal
        if len(set(values)) != 1:
            return False
        
        #no duplicates
        l = [number for row in square for number in row]
        if len(l) != len(set(l)):
            return False
        
        return True