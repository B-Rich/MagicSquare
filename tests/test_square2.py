import unittest
from square2 import Square2 as S2

class TestSquare2(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_load(self):
        magic_3 = [[8,1,6],[3,5,7],[4,9,2]]
        test_obj_3 = S2(3)
        test_obj_3.load(magic_3)
        self.assertListEqual(test_obj_3, magic_3)
        
    def test__hash_(self):
        test_obj_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        test_obj_3_r = S2(3, [[4,3,8],[9,5,1],[2,7,6]])
        self.assertEqual(test_obj_3._hash_(), test_obj_3_r._hash_())
        
    def test_rotate(self):
        test_obj_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        test_obj_3_r = S2(3, [[4,3,8],[9,5,1],[2,7,6]])
        test_obj_3.rotate()
        self.assertListEqual(test_obj_3, test_obj_3)
        
    def test_populateRandom(self):
        test_obj_3 = S2(3)
        test_obj_3.populateRandom()
        self.assertIs(type(test_obj_3[0]), list)
        self.assertIs(type(test_obj_3[0][0]), int)
        
    def test_loadFlat(self):
        flat_3 = [8,1,6,3,5,7,4,9,2]
        magic_3 = [[8,1,6],[3,5,7],[4,9,2]]
        test_obj_3 = S2(3)
        test_obj_3f = S2(3)
        test_obj_3.load(magic_3)
        test_obj_3f.loadFlat(flat_3)
        self.assertListEqual(test_obj_3, test_obj_3f)
        
    def test_getTotals(self):
        magic_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        totals = ((15, 15, 15),
                  (15, 15, 15),
                  (15, 15))
        self.assertTupleEqual(magic_3.getTotals(), totals)
        
    def test_isEmpty(self):
        magic_3 = S2(3, [[8,1,6],[3,5,7],[4,9,2]])
        magic_4 = S2(4)
        self.assertTrue(magic_4.isEmpty())
        self.assertFalse(magic_3.isEmpty())
        
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestSquare2)
unittest.TextTestRunner(verbosity=4).run(suite)