from typing import Callable, Iterable, TypeVar

from pylinq.enumerable import enumerable
from pylinq.pydict import pydict

T = TypeVar("T")
U = TypeVar("U")
TKey = TypeVar("TKey")
TValue = TypeVar("TValue")

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
         
    def as_enumerable(self):
        return enumerable(self)
    