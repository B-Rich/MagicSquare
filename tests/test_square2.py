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
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestSquare2)
unittest.TextTestRunner(verbosity=4).run(suite)