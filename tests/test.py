import unittest
from pylinq import pylist
from pylinq import pydict

class PylistTest(unittest.TestCase):
    
    l = pylist([1,2,3,4,5,6,7,8,9,0])
        
    def test_where(self):
        self.assertEqual(
            self.l.where(lambda x: x%2==0),
            [2,4,6,8,0]
        )
    
    def test_select(self):
        self.assertEqual(
            self.l.select(lambda x: str(x)),
            ["1","2","3","4","5","6","7","8","9","0"]
        )
    
    def test_take(self):
        self.assertEqual(
            self.l.take(3),
            [1,2,3]
        )
        
    def test_take_while(self):
        self.assertEqual(
            self.l.take_while(lambda x :x[0] < 3 and x[1] < 5),
            [1,2]
        )
    
    def test_average(self):
        self.assertEqual(
            self.l.average(),
            4.5
        )

    def test_sum_numeric(self):
        self.assertEqual(self.l.sum(), 45)
        
    def test_countif(self):
        self.assertEqual(
            self.l.countif(lambda x: x > 5),
            4
        )
        
    def test_contains_1(self):
        self.assertEqual(self.l.contains(5), True)
    
    def test_contains_2(self):
        self.assertEqual(self.l.contains(10), False)
    
    def test_first_1(self):
        self.assertEqual(self.l.first(), 1)
    
    def test_first_2(self):
        self.assertEqual(self.l.first(lambda x: x > 3), 4)
    
    def test_first_3(self):
        with self.assertRaises(Exception):
            pylist().first()
            
    def test_first_or_default_1(self):
        self.assertEqual(self.l.first_or_default(), 1)
        
    def test_first_or_default_2(self):
        self.assertEqual(pylist().first_or_default(), None)
        
    def test_first_or_default_3(self):
        self.assertEqual(self.l.first_or_default(lambda x: x > 3), 4)
                         
    def test_concat(self):
        self.assertEqual(
            self.l.concat(["a","b"]),
            [1,2,3,4,5,6,7,8,9,0,"a","b"]
        )

if __name__ == "__main__":
    unittest.main()