import unittest
from squares import Square as S

class TestSquare(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_generateRowValues(self):
        t1 = [[1,14,14,4],
              [11,7,6,9],
              [8,10,10,5],
              [13,2,3,15]]
        s1 = S(4)
        s1.importSquare(t1)
        r1 = {'row': {(0,0): 33,
                      (1,0): 33,
                      (2,0): 33,
                      (3,0): 33},
              'col': {(0,0): 33,
                      (0,1): 33,
                      (0,2): 33,
                      (0,3): 33},
              'dia': {(0,0): 33,
                      (3,0): 33},
              'dis': (33, 33, 33, 33, 33, 33, 33, 33, 33, 33)
              }
        
        self.assertEqual(s1.generateRowValues(), r1)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSquare)
unittest.TextTestRunner(verbosity=4).run(suite)
