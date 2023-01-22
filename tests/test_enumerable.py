import unittest

from pylinq.pylinq import enumerable, pylist, pydict

class TestInnerClass:
    name = ""
    piyo = 0
    def __init__(self,n,p):
        self.name=n
        self.piyo=p
class TestClass:
    name = ""
    hoge = []
    def __init__(self,n,h):
        self.name=n
        self.hoge=h
    
class enumerableTest(unittest.TestCase):

    e = enumerable([1,2,3,4,5,6,7,8,9,0])
    a1 = TestInnerClass("A1",1)
    a2 = TestInnerClass("A2",2)
    b1 = TestInnerClass("B1",3)
    b2 = TestInnerClass("B2",4)
    
    a = TestClass("a", [a1, a2])
    b = TestClass("b", [b1, b2])
        
    test = [a ,b]
    
    def test_readme(self):
        
        e = enumerable([1,2,3,4,5,6,7,8,9,0])
        
        e.where(lambda x: x % 2 == 0)\
            .select(lambda x: x * x)\
            .where(lambda x: 30 < x)\
            .to_pylist()\
            .for_each(lambda x: print(x))
            
    def test_range(self):
        self.assertEqual(
            enumerable.range(1,9).to_list(),
            [1,2,3,4,5,6,7,8,9]
        )
        
    def test_repeat(self):
        self.assertEqual(
            enumerable.repeat(7,7).to_list(),
            [7,7,7,7,7,7,7]
        )
        
    def test_to_list(self):
        self.assertEqual(
            self.e.to_list(),
            [1,2,3,4,5,6,7,8,9,0]
        )
        
    def test_to_readonly_pylist(self):
        r = enumerable([1,2,3]).to_readonly_pylist()
        self.assertEqual(r, (1,2,3))
        with self.assertRaises(NotImplementedError):
            r[1] = 10
        
    def test_to_pylist(self):
        self.assertEqual(
            self.e.to_pylist(),
            [1,2,3,4,5,6,7,8,9,0]
        )
        
    def test_to_dict(self):
        self.assertEqual(
            enumerable.range(1,3).to_dict(lambda x:x),
            {1:1, 2:2, 3:3}
        )
        self.assertEqual(
            enumerable.range(1,3).to_dict(lambda x:x, lambda x:str(x*x)),
            {1:"1", 2:"4", 3:"9"}
        )
    
    def test_where(self):
        self.assertEqual(
            self.e.where(lambda x: x < 5).to_list(),
            [1,2,3,4,0]
        )
    
    def test_select(self):
        self.assertEqual(
            self.e.select(lambda x: str(x)).to_list(),
            ["1","2","3","4","5","6","7","8","9","0"]
        )

    def test_take(self):
        self.assertEqual(
            self.e.take(3).to_list(),
            [1,2,3]
        )
        
    def test_take_while(self):
        self.assertEqual(
            self.e.take_while(lambda x, i: x < 5 and i < 3).to_list(),
            [1,2,3]
        )
        
    def test_skip(self):
        self.assertEqual(
            self.e.skip(3).to_list(),
            [4,5,6,7,8,9,0]
        )
        
    def test_skip_while(self):
        self.assertEqual(
            self.e.skip_while(lambda x, i: x < 5 and i < 3).to_list(),
            [4,5,6,7,8,9,0]
        )
        
    def test_first_1(self):
        self.assertEqual(
            self.e.first(),
            1
        )
        
    def test_first_2(self):
        self.assertEqual(
            self.e.first(lambda x: 6 < x),
            7
        )
    
    def test_first_3(self):
        with self.assertRaises(Exception):
            enumerable([]).first(lambda x: 6 < x)
            
    def test_first_or_default(self):
        self.assertEqual(
            enumerable([]).first_or_default(lambda x: 6 < x),
            None
        )
        
    def test_last_1(self):
        self.assertEqual(self.e.last(), 0)
    
    def test_last_2(self):
        self.assertEqual(
            self.e.last(lambda x: 6 < x),
            9
        )
    
    def test_element_at(self):
        self.assertEqual(
            self.e.element_at(5),
            6
        )
        
    def test_select_many(self):
        self.assertEqual(
            enumerable(self.test).select_many(lambda x: x.hoge).to_list(),
            [self.a1, self.a2, self.b1, self.b2]
        )
        self.assertEqual(
            enumerable(self.test).select_many(lambda x: x.name).to_list(),
            ["a", "b"]
        )

    def test_distinct(self):
        self.assertEqual(
            enumerable([1,1,2,2,3,3,5,5,4,4]).distinct().to_list(),
            [1,2,3,5,4]
        )
        
    def test_distinct_by(self):
        test_data = [self.a1, self.b2, self.a1, self.b1]
        test_data.append(TestInnerClass("B1", None))
        self.assertEqual(
            enumerable(test_data).distinct_by(lambda x:x.name).to_list(),
             [self.a1, self.b2, self.b1]
        )
    
    def test_sum(self):
        self.assertEqual(self.e.sum(), 45)
        self.assertEqual(self.e.sum(lambda x: x < 5), 10)
    
    def test_average(self):
        self.assertEqual(self.e.average(), 4.5)
        self.assertEqual(self.e.average(lambda x: x < 5), 2)
    
    def test_count(self):
        self.assertEqual(self.e.count(lambda x: x > 5), 4)
    
    def test_max(self):
        self.assertEqual(self.e.max(), 9)
        
        data = enumerable([self.a1,self.a2,self.b1,self.b2])
        self.assertEqual(data.max(lambda x: x.piyo), 4)
        
    def test_min(self):
        self.assertEqual(self.e.min(), 0)
        
        data = enumerable([self.a1,self.a2,self.b1,self.b2])
        self.assertEqual(data.min(lambda x: x.piyo), 1)
        
    def test_all(self):
        self.assertEqual(self.e.all(lambda x: 0 <= x), True)
        self.assertEqual(self.e.all(lambda x: 1 <= x), False)
        
    def test_min(self):
        self.assertEqual(self.e.any(), True)
        self.assertEqual(enumerable([]).any(), False)
        self.assertEqual(self.e.any(lambda x: 9 < x), False)
        self.assertEqual(self.e.any(lambda x: 8 < x), True)
        
    def test_concat(self):
        a = enumerable([1,2,3])
        b = list([4,5])
        self.assertEqual(a.concat(b).to_list(), enumerable([1,2,3,4,5]).to_list())
        
    def test_contains(self):
        self.assertEqual(self.e.contains(3), True)
        self.assertEqual(self.e.contains(11), False)
    
    def test_union(self):
        a = pylist([2,4,5,6,8])
        b = pylist([1,3,5,7,8,9])
        
        self.assertEqual(a.union(b).to_list(),[2,4,5,6,8,1,3,7,9])
        
    def test_set_difference(self):
        a = pylist([2,4,5,6,8])
        b = pylist([1,3,5,7,8,9])
        
        self.assertEqual(a.set_difference(b).to_list(),[2,4,6])
    
    def test_intersect(self):
        a = pylist([2,4,5,6,8])
        b = pylist([1,3,5,7,8,9])
        
        self.assertEqual(a.intersect(b).to_list(),[5,8])
        
    def test_zip(self):
        a = pylist([1,2,3,4])
        b = pylist(["A","B","C","D","E","F"])
        
        self.assertEqual(
            a.zip(b, lambda f,s:(f,s)).to_list(),
            [(1,"A"), (2,"B"),(3,"C"),(4,"D")]
            )
        
    def test_single(self):
        a = pylist([1, 3, 5, 6, 8, 5])
        
        with self.assertRaises(Exception):
            pylist([]).single()
        
        with self.assertRaises(Exception):
            pylist(a).single(lambda x:5<x)
                    
        self.assertEqual(pylist([3]).single(),3)
        self.assertEqual(pylist(a).single(lambda x:x>7),8)
        
    def test_aggregate(self):
        a = pylist([1,2,3,4,5])
        
        self.assertEqual(
            a.aggregate(10, lambda ret, current: ret + current, lambda x:x*x),
            (10+1+2+3+4+5)*(10+1+2+3+4+5)
        )
        
    def test_chunk(self):
        self.assertEqual(
            self.e.chunk(3),
            [[1,2,3],[4,5,6],[7,8,9],[0]]
        )
if __name__ == "__main__":
    unittest.main()