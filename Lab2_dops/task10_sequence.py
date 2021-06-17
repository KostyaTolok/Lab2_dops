class Sequence:

    def __init__(self, iterable=None):
        try:
            iter(iterable)
        except TypeError:
            raise

        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)

    def filter(self, func):
        res = []
        for val in self.iterable:
            if func(val):
                res.append(val)
        return Sequence(res)

    def __repr__(self):
        return str(self.iterable)


def is_int(value):
    return isinstance(value, int)


s = Sequence(("asd", 2, "a", 2.3))

for i in s:
    print(i)

for i in s.filter(is_int):
    print(i)
