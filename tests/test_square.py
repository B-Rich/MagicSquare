import unittest
from squares import Square

class TestSquare(unittest.TestCase):
    
    def setUp(self):
        pass
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestSquare)
unittest.TextTestRunner(verbosity=4).run(suite)