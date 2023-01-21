from typing import Callable, Iterable, TypeVar
import pylinq
from pylinq.enumerable import enumerable

T = TypeVar("T")
U = TypeVar("U")
TKey = TypeVar("TKey")
TValue = TypeVar("TValue")

class pydict(dict, enumerable):
    def __init__(self, ite:Iterable[T]):
        super(pydict, self).__init__(ite)
        self._ite = self
        self._index = 0
    
    def to_pylist(self) :
        ret = pylinq.pylist()
        for e in self.items():
            ret.append(e)
        return ret