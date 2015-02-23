import unittest
from magicsquare import MagicSquare as M

class TestUnitSquare(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_generateOdd(self):
        t1 = [[8,1,6],
              [3,5,7],
              [4,9,2]]
        t2 = [[9,2,7],
              [4,6,8],
              [5,10,3]]
        t3 = [[15,1,11],
              [5,9,13],
              [7,17,3]]
        
        self.assertRaises(ValueError, M().generateOdd, 4)
        self.assertEqual(M().generateOdd(3), t1)
        self.assertEqual(M().generateOdd(3, initial=2), t2)
        self.assertEqual(M().generateOdd(3, increment=2), t3)
        
    def test_testMagic(self):
        t1 = [[8,1,6],
              [3,5,7],
              [4,9,2]]
        t2 = [[9,2,7],
              [4,6,8],
              [5,10,3]]
        t3 = [[15,1,11],
              [5,9,13],
              [7,17,3]]
        t4 = [[15,1,11],
              [5,9,13],
              [7,17,99]]
        t5 = [[1,14,14,4],
              [11,7,6,9],
              [8,10,10,5],
              [13,2,3,15]]
        t6 = [[1,5,9],
              [6,7,2],
              [8,3,4]]
        
        #line counts
        self.assertTrue(M().testMagic(t1))
        self.assertTrue(M().testMagic(t2))
        self.assertTrue(M().testMagic(t3))
        self.assertFalse(M().testMagic(t4))
        #duplicate numbers
        self.assertFalse(M().testMagic(t5))
        #diagonals
        self.assertFalse(M().testMagic(t6))
     
    def test_testSemiMagic(self):
        t1 = [[8,1,6],
              [3,5,7],
              [4,9,2]]
        t2 = [[1,14,14,4],
              [11,7,6,9],
              [8,10,10,5],
              [13,2,3,15]]
        t3= [[1,5,9],
              [6,7,2],
              [8,3,4]]
        
        #magic
        self.assertFalse(M().testSemiMagic(t1))
        #duplicate numbers
        self.assertFalse(M().testSemiMagic(t2))
        #semi-magic
        self.assertTrue(M().testSemiMagic(t3))
        
    
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestUnitSquare)
unittest.TextTestRunner(verbosity=4).run(suite)
