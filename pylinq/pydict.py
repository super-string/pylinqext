import pylinq

class pydict(dict):
    def to_pylist(self) :
        ret = pylinq.pylist()
        for e in self.items():
            ret.append(e)
        return ret