from __future__ import annotations
from typing import Callable, Generic, Iterable, Iterator, TypeVar, TYPE_CHECKING

T = TypeVar("T")
U = TypeVar("U")
TKey = TypeVar("TKey")
TValue = TypeVar("TValue")

class enumerable(Iterator[T], Generic[T]):
    def __init__(self, ite:Iterable[T]):
        self._ite = ite
        self._index = 0
        
    def __next__(self):
        try:
            val = self._ite[self._index]
            self._index += 1
            return val
        except:
            raise StopIteration
        
    def __iter__(self) -> Iterator[T]:
        for e in self._ite:
            yield e
    
    def __select_many_iter(self, selector:Callable[[T], list[U]]):
        for src in self._ite:
            for ret in selector(src):
                yield ret
        
    def __cond_iter(self, cond:Callable[[T], bool]):
        for e in self._ite:
            if cond(e):
                yield e
    
    @staticmethod
    def range(start, end):
        return enumerable(range(start, end))
    
    def to_list(self) -> list:
        return list(self._ite)
    
    def to_pylist(self) -> pylist:
        return pylist(self._ite)
    
    def to_dict(self, key_selector:Callable[[T], TKey], value_selector:Callable[[T], TValue] = None) -> dict:
        dic = {}
        for e in self._ite:
            if value_selector == None:
                dic[key_selector(e)] = e
            else:
                dic[key_selector(e)] =value_selector(e)
        return dic 
    
    def where(self, cond:Callable[[T], bool]):
        return enumerable([e for e in self.__cond_iter(cond)])
    
    def select(self, selector:Callable[[T], U]):
        return enumerable([selector(e) for e in self.__iter__()])
    
    def select_many(self, selector:Callable[[T], list[U]]):
        return enumerable([e for e in self.__select_many_iter(selector)])
        
    def take(self, count):
        i = 0
        ret = []
        for e in self.__iter__():
            if i < count:
                ret.append(e)
            else:
                break
            i += 1
        return enumerable(ret)
    
    def take_while(self, cond:Callable[[T, int], bool]):
        i = 0
        ret = []
        for e in self.__iter__():
            if not cond(e, i):
                break
            ret.append(e)
            i += 1
        return enumerable(ret)
            
    def skip(self, count):
        i = 0
        ret = []
        for e in self.__iter__():
            if i < count:
                pass
            else:
                ret.append(e)
            i += 1
        return enumerable(ret)
    
    def skip_while(self, cond:Callable[[T, int], bool]):
        i = 0
        ret = []
        for e in self.__iter__():
            if cond(e, i):
                pass
            else:
                ret.append(e)
            i += 1
        return enumerable(ret)
    
    def first(self, cond:Callable[[T], bool] = None):
        if cond == None:
            return self.to_list()[0]
        
        for e in self.__iter__():
            if cond(e):
                return e
            
        raise Exception("not found")
    
    def first_or_default(self, cond:Callable[[T], bool] = None):
        try:
            return self.first(cond)
        except:
            return None
        
    def last(self, cond:Callable[[T], bool] = None):
        l = list(self._ite)
        l.reverse()
        return enumerable(l).first(cond)
            
    def last_or_default(self, cond:Callable[[T], bool] = None):
        try:
            return self.last(cond)
        except:
            return None
        
    def element_at(self, index):
        return self._ite[index]
    
    def element_at_or_default(self, index):
        try:
            return self._ite[index]
        except:
            return None
        
    def single(self, cond:Callable[[T], bool] = None):
        pass
    
    def single_or_default(self, cond:Callable[[T], bool] = None):
        pass
    
    def default_if_empty(self):
        pass
    
    def __distinct_iter(self):
        s = set()
        for e in self._ite:
            if not s.__contains__(e):
                s.add(e)
                yield e
                
    def distinct(self):
        return enumerable([e for e in self.__distinct_iter()])
    
    def average(self):
        return self.sum() / len(self._ite)
    
    def sum(self):
        total = 0
        for e in self._ite:
            total += e
        return total
    
    def aggregate(self):
        pass
    
    def count(self, cond:Callable[[T], bool]):
        cnt = 0
        for _ in self.__cond_iter(cond):
            cnt += 1
        return cnt
    
    def max(self):
        val = self._ite[0]
        for e in self._ite:
            if val < e:
                val = e
        return val
    
    def min(self):
        val = self._ite[0]
        for e in self._ite:
            if val > e:
                val = e
        return val

    def all(self, cond:Callable[[T], bool]) -> bool:
        for e in self._ite:
            if not cond(e):
                return False
        return True
    
    def any(self, x : Callable = None) -> bool:
        if x == None:
            return 0 < len(self._ite)
        for e in self._ite:
            if x(e):
                return True
        return False
    
    def concat(self, second :list):
        pass
    def contains(self, value) -> bool:
        pass
    def aggregate(self, x : Callable):
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
    def order_by(self):
        pass
    def order_by_descending(self):
        pass
    def union(self):
        pass
    def zip(self):
        pass
    
class pylist(list, enumerable):
    def __init__(self, ite:Iterable[T]):
        super(pylist, self).__init__(ite)
        self._ite = self
        self._index = 0

    def for_each(self, action:Callable[[T], None]):
        for e in self.__iter__():
            action(e)
            
    def to_pydict(self, key_selector:Callable[[T], TKey], value_selector:Callable[[T], TValue] = None):
        return pydict(self.to_dict(key_selector, value_selector))
         
    def as_enumerable(self) -> enumerable:
        return enumerable(self)
    

class pydict(dict, enumerable):
    def __init__(self, ite:Iterable[T]):
        super(pydict, self).__init__(ite)
        self._ite = self
        self._index = 0
    
    def to_pylist(self) :
        ret = pylist()
        for e in self.items():
            ret.append(e)
        return ret