![GitHub](https://img.shields.io/github/license/super-string/pylinq)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/super-string/pylinq)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/super-string/pylinq)
# pylinq
pylinq is a package for C#er to write code like LINQ.

## Usage
```python
from pylinq import pylist
from pylinq import enumerable
  
e = enumerable([1,2,3,4,5,6,7,8,9,0])
  
e.where(lambda x: x % 2 == 0)\
        .select(lambda x: x * x)\
        .where(lambda x: 30 < x)\
        .to_pylist()\
        .for_each(lambda x: print(x))
```
Output:
```
36
64
```

## Install
```
pip install git+https://github.com/super-string/pylinq
```

## Version
- v0.0.1-alpha
    - first commit
- v0.0.2
    - implement single, aggregate, etc
- v0.0.3
    - readonlylist, some methods
- v0.5.0
    - renampe project to pylinqext
## class
- enumerable
- pylist
- pydict
- pyreadonlylist

## Support
〇：implemented  
△：not implemented  
×：not suppot  
|Support|Method|Memo|
|---|---|---|
|〇|aggregate||
|〇|all||
|〇|any||
|〇|append||
|〇|as_enumerable|implemented to pylist|
|〇|average||
|×|cast||
|〇|chunk||
|〇|concat||
|〇|contains||
|〇|count||
|×|default_if_empty||
|〇|distinct||
|〇|distinct_by||
|〇|element_at||
|〇|element_at_or_default||
|×|empty||
|〇|except|named:`set_difference`|
|〇|except_by|named:`set_difference_by`|
|〇|first||
|〇|first_or_default||
|×|group_by||
|×|group_join||
|〇|intersect||
|△|intersect_by||
|〇|max||
|△|max_by||
|〇|min||
|△|min_by||
|〇|of_type||
|×|order||
|×|order_by||
|×|order_by_descending||
|×|order_descending||
|〇|prepend||
|〇|range||
|〇|repeat||
|〇|reverse||
|〇|select||
|〇|select_many||
|×|sequential_equal||
|〇|single||
|〇|single_or_default||
|〇|skip||
|△|skip_last||
|〇|skip_while||
|〇|sum||
|〇|take||
|△|take_last||
|〇|take_while||
|×|then_by||
|×|then_by_descending||
|×|to_array||
|〇|to_dict||
|△|to_set||
|〇|to_list|use `to_pylist` to write method chain.|
|×|to_lookup||
|〇|to_readonly_list||
|〇|union||
|△|union_by||
|〇|where||
|〇|zip||
