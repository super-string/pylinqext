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
        self.assertEqual(r, (1,2,3))
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
        
    def test_items(self):
        self.assertEqual(
            self.l.items(),
            [(1,1),(2,2),(3,3)]
        )
        self.assertEqual(
            self.l.items().where(lambda x: x[0] >= 2).to_list(),
            [(2,2),(3,3)]
        )
        self.assertEqual(
            self.l.items().where(lambda x: x[0] >= 2).to_dict(lambda x:x[0], lambda x:x[1]),
            {2:2, 3:3}
        )
        
    def test_keys(self):
        self.assertEqual(
            self.l.keys().select(lambda x:x*x).to_list(),
            [1,4,9]
        )
        
    def test_values(self):
        self.assertEqual(
            self.l.values().select(lambda x:x*x).to_list(),
            [1,4,9]
        )
    
    def test_copy(self):
        cp = self.l.copy()
        cp[1] = 0
        self.assertEqual(
            cp,
            {1:0, 2:2, 3:3}
        )
    
    def test_a(self):
        d = self.l.copy()
        d.add_if_not_exists(1,2)
        print(d)
        d.add_if_not_exists("a",2)
        print(d)
                    
if __name__ == "__main__":
    unittest.main()
    

from pylinqext import enumerable, pydict

d = pydict({1:1, 2:2, 3:3})
d.items()\
    .where(lambda x: x[0] >= 2)\
    .to_pydict(lambda x:x[0], lambda x:x[1])\
    .for_each(lambda k,v: print(f"key={k},value={v}"))