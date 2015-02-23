import random

class Square(object):
    def __init__(self, order):
        self.order = order
        self.square = []
        #Create empty square
        for _ in xrange(self.order):
            line = []
            for _ in xrange(self.order):
                line.append(None)
            self.square.append(line)
        
    def printSquare(self):
        for row in self.square:
            print(row)

class CandidateSquare(Square):
    def __init__(self, order):
        Square.__init__(self, order)
        
        for x in xrange(self.order):
            for y in xrange(self.order):
                self.square[y][x] = random.randrange(1, self.order**2)
                
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
        for x in xrange(self.order):
            p = 0
            for row in self.square:
                p += row[x]
            values.append(p)
        #diagonals
        x1, y1 = 0, 0
        x2, y2 = self.order -1, 0
        d1, d2 = 0, 0
        for _ in xrange(self.order):
            d1 += self.square[y1][x1]
            d2 += self.square[y2][x2]
            y1 += 1
            x1 += 1
            y2 += 1
            x2 -= 1
        values.append(d1)
        values.append(d2)
        
        print values

if __name__ == '__main__':
    A = CandidateSquare(3)
    A.printSquare()
    A.evaluateFitness()