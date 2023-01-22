from __future__ import annotations
from typing import Any, Callable, Generic, Iterable, Iterator, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .pylinq import pylist, pydict
    
T = TypeVar("T")
U = TypeVar("U")
S = TypeVar("S")
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
        
    def __cond_iter(self, cond:Callable[[T], bool]):
        for e in self._ite:
            if cond(e):
                yield e
    
    @staticmethod
    def range(start:int, count:int):
        def seq(start, count):
            for e in range(start, start + count):
                yield e
        return enumerable([e for e in seq(start, count)])
    
    @staticmethod
    def repeat(value: T, count:int):
        def seq(value: T, count):
            for _ in range(count):
                yield value
        return enumerable([e for e in seq(value, count)])
            
    
    def to_list(self) -> list:
        return list(self._ite)
    
    def to_pylist(self) -> pylist:
        return pylist(self._ite)
    
    def to_dict(self, key_selector:Callable[[T], TKey], value_selector:Callable[[T], TValue] = lambda x:x) -> dict:
        dic = {}
        for e in self._ite:
            dic[key_selector(e)] = value_selector(e)
        return dic 
    
    def where(self, cond:Callable[[T], bool]):
        return enumerable([e for e in self.__cond_iter(cond)])
    
    def select(self, selector:Callable[[T], U]):
        return enumerable([selector(e) for e in self.__iter__()])
    
    def select_many(self, selector:Callable[[T], list[U]]):
        def seq(selector:Callable[[T], list[U]]):
            for src in self._ite:
                for ret in selector(src):
                    yield ret
        return enumerable([e for e in seq(selector)])
        
    def take(self, count):
        return self.take_while(lambda _,i: i < count)
    
    def take_while(self, cond:Callable[[T, int], bool]):
        def seq():
            i = 0
            for e in self.__iter__():
                if not cond(e, i):
                    break
                yield e
                i += 1
        return enumerable([e for e in seq()])
            
    def skip(self, count):
        return self.skip_while(lambda _, i: i < count)
    
    def skip_while(self, cond:Callable[[T, int], bool]):
        def seq():
            i = 0
            for e in self.__iter__():
                if cond(e, i):
                    pass
                else:
                    yield e
                i += 1
        return enumerable([e for e in seq()])
    
    def first(self, cond:Callable[[T], bool] = lambda x:True):
        if cond == None:
            return self.to_list()[0]
        
        for e in self.__iter__():
            if cond(e):
                return e
            
        raise Exception("not found")
    
    def first_or_default(self, cond:Callable[[T], bool] = lambda x:True):
        try:
            return self.first(cond)
        except:
            return None
        
    def last(self, cond:Callable[[T], bool] = lambda x:True):
        l = list(self._ite)
        l.reverse()
        return enumerable(l).first(cond)
            
    def last_or_default(self, cond:Callable[[T], bool] = lambda x:True):
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
        
    def single(self, cond:Callable[[T], bool] = lambda x:True):
        ret = None
        found = 0
        for e in self.__cond_iter(cond):
            ret = e
            found += 1
        
        if found == 0:
            raise Exception("no element")
        if found == 1:
            return ret
        raise Exception("more than one element")
    
    def single_or_default(self, cond:Callable[[T], bool] = lambda x:True):
        try:
            self.single(cond)
        except:
            return None
    
    def default_if_empty(self):
        pass
    
    def distinct(self):
        def __distinct_iter():
            s = set()
            for e in self._ite:
                if not s.__contains__(e):
                    s.add(e)
                    yield e
        
        return enumerable([e for e in __distinct_iter()])
    
    def average(self, selector:Callable[[T], bool] = lambda x:True):
        return self.sum(selector) / self.count(selector)
    
    def sum(self, selector:Callable[[T], bool] = lambda x:True):
        total = 0
        for e in self._ite:
            if selector(e):
                total += e
        return total
    
    def aggregate(self):
        pass
    
    def count(self, cond:Callable[[T], bool]= lambda x:True):
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
    
    def any(self, x : Callable[[T], bool] = lambda x: True) -> bool:
        for e in self._ite:
            if x(e):
                return True
        return False
    
    def concat(self, second: Iterable[T]):
        def seq(first: Iterable[T], second: Iterable[T]):
            for e in first:
                yield e
            for e in second:
                yield e
        return enumerable([e for e in seq(self._ite, second)])

    def contains(self, value) -> bool:
        for e in self._ite:
            if e == value:
                return True
        return False
    
    def aggregate(self, x : Callable):
        pass
    
    def union(self, second: Iterable[T]):
        def seq(first: Iterable[T], second: Iterable[T]):
            s = set()
            for e in first:
                if not s.__contains__(e):
                    yield e
                    s.add(e)
            for e in second:
                if not s.__contains__(e):
                    yield e
                    s.add(e)
            
        return enumerable([e for e in seq(self._ite, second)])
        
    def set_difference(self, second: Iterable[T]):# in C# : Except
        def seq(first: Iterable[T], second: Iterable[T]):
            s = set()
            for e in second:
                s.add(e)
            for e in first:
                if not s.__contains__(e):
                    yield e
                    s.add(e)
        return enumerable([e for e in seq(self._ite, second)])
    
    def intersect(self, second: Iterable[T]):
        def seq(first: Iterable[T], second: Iterable[T]):
            s = set()
            for e in second:
                s.add(e)
            for e in first:
                if s.__contains__(e):
                    yield e
                    s.remove(e)
        return enumerable([e for e in seq(self._ite, second)])
    
    def group_by(self):
        pass
    def group_join(self):
        pass
    def join(self):
        pass
    def order_by(self):
        pass
    def order_by_descending(self):
        pass
    def zip(self, second:Iterable[U], selector:Callable[[T, U], S]):
        def seq(first:Iterable, second:Iterable[U], selector:Callable[[T, U], S]):
            f = next(first, None)
            s = next(second, None)
            while f != None and s != None:
                yield selector(f, s)
                f = next(first, None)
                s = next(second, None)
                
        return enumerable([e for e in seq(self._ite, second, selector)])
    
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
        return pylist([e for e in self.items()])