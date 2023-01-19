from traitlets import Callable

import pylinq
from pylinq.pydict import pydict

class pylist(list):
    def for_each(self, x : Callable):
        for e in self:
            x(e)
    
    def where(self, x : Callable) :
        ret = pylist()
        for e in self:
            if x(e) :
                ret.append(e)
        return ret
    
    def take(self, count) :
        index = 0
        ret = pylist()
        for e in self:
            if index < count:
                ret.append(e)
            index += 1
        return ret
    
    def take_while(self, x : Callable) :
        ret = pylist()
        index = 0
        for e in self:
            if x((e, index)) :
                ret.append(e)
            index += 1
        return ret
        
    def select(self, x : Callable):
        return pylist([x(e) for e in self])
        
    def to_dict(self, x : Callable) ->dict:
        ret = {}
        for e in self:
            (k, v) = x(e)
            ret[k] = v
        return ret
    
    def to_pydict(self, x : Callable) ->pydict:
        ret = pydict()
        for e in self:
            (k, v) = x(e)
            ret[k] = v
        return ret
    
    def all(self, x : Callable) -> bool:
        for e in self:
            if x(e) == False:
                return False
        return True
    
    def any(self, x : Callable = None) -> bool:
        if x == None:
            return 0 < len(self)
        for e in self:
            if x(e):
                return True
        return False
    
    def first(self, x : Callable = None):
        if x == None:
            return self[0]
        for e in self:
            if x(e):
                return e
        raise Exception("element not found")
    
    def first_or_default(self, x : Callable = None):
        if len(self) == 0:
            return None
        if x == None:
            return self[0]
        for e in self:
            if x(e):
                return e
        return None
    
    def countif(self, x : Callable) -> int:
        count = 0
        for e in self:
            if x(e) == True:
                count += 1
        return count
    
    def contains(self, value) -> bool:
        for e in self:
            if e == value:
                return True
        return False
        
    def sum(self):
        ret = 0
        for e in self:
            ret += e
        return ret
        
    def average(self):
        """average
        calc average.
        if no element in the list, raise exception.
        """
        return self.sum() / len(self)
    
    def concat(self, second :list):
        ret = pylist(self)
        pylist(second).for_each(lambda x: ret.append(x))
        return ret
    
    def aggregate(self, x : Callable):
        pass
    def distinct(self):
        pass
    def pyexcept(self):# 名前考える
        pass
    def group_by(self):
        pass
    def group_join(self):
        pass
    def intersect(self):
        pass
    def join(self):
        pass
    def last(self):
        pass
    def last_or_default(self):
        pass
    def max(self):
        val = self[0]
        for e in self:
            if val < e:
                val = e
        return val
    def min(self):
        val = self[0]
        for e in self:
            if val > e:
                val = e
        return val
    def order_by(self):
        pass
    def order_by_descending(self):
        pass
    def single(self):
        pass
    def single_or_default(self):
        pass
    def skip(self):
        pass
    def skip_or_default(self):
        pass
    def skip_while(self):
        pass
    def union(self):
        pass
    def zip(self):
        pass