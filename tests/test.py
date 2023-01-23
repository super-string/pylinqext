import unittest

from pylinqext import pylist, pydict, pyreadonlylist

class pylistTest(unittest.TestCase):
    
    l = pylist([1,2,3,4,5,6,7,8,9,0])
        
    def test_to_pydict(self):
        data = pylist([1,2,3])
        self.assertEqual(
            data.to_pydict(lambda x:x, lambda x:x*x),
            { 1:1, 2:4, 3:9 }
        )

    def test_as_enumerable(self):
        e = self.l.as_enumerable()
        self.assertEqual(e.to_pylist(), self.l)
        
    def test_readonly(self):
        r = pyreadonlylist([1,2,3])
        self.assertEqual(r, [1,2,3])
        with self.assertRaises(NotImplementedError):
            r[1] = 10

class pydictTest(unittest.TestCase):
    
    l = pydict({1:1, 2:2, 3:3})
        
    def test_to_pylist(self):
        expected = pylist([(1,1),(2,2),(3,3)])
        self.assertEqual(
            self.l.to_pylist(),
            expected
        )
                
if __name__ == "__main__":
    unittest.main()
    