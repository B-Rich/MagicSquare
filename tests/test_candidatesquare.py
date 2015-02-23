import unittest
from squares import CandidateSquare

class TestCandidateSquare(unittest.TestCase):
    
    def setUp(self):
        pass
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestCandidateSquare)
unittest.TextTestRunner(verbosity=4).run(suite)