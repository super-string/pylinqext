# pylinq
pylinq is a package for C#er to write code like LINQ.

## Usage
```python
from pylinq import pylist
from pylinq import enumerable
  
e = enumerable([1,2,3,4,5,6,7,8,9,0])
  
ret = e.where(lambda x: x % 2 == 0)\
        .select(lambda x: x * x)\
        .where(lambda x: 30 < x)\
        .to_list()
  
pylist(ret).for_each(lambda x: print(x))
```
Outpu:
```
36
64
```

