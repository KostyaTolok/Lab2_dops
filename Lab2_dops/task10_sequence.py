class Sequence:

    def __init__(self, *args):
        self.values = [*args]

    def __iter__(self):
        return iter(self.values)

    def filter(self, func):
        res = []
        for val in self.values:
            if func(val):
                res.append(val)
        return res


def is_int(value):
    return isinstance(value, int)


s = Sequence(6, 3, "asd", 1, 12.22)

for i in s.filter(is_int):
    print(i)

for i in s:
    print(i)