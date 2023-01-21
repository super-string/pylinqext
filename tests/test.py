import unittest

from pylinq import pydict, pylist

class pylistTest(unittest.TestCase):
    
    l = pylist([1,2,3,4,5,6,7,8,9,0])
        
    def test_to_pydict(self):
        data = pylist([1,2,3])
        self.assertEqual(
            data.to_pydict(lambda x:x, lambda x:x*x),
            { 1:1, 2:4, 3:9 }
        )


class pydictTest(unittest.TestCase):
    
    l = pydict({1:1, 2:2, 3:3})
        
    def test_to_pydict(self):
        data = pylist([1,2,3])
        self.assertEqual(
            data.to_pydict(lambda x:x, lambda x:x*x),
            { 1:1, 2:4, 3:9 }
        )
                
if __name__ == "__main__":
    unittest.main()
    