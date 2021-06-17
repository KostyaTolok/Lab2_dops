class DefaultDict:

    def __init__(self, value=None):
        self.dic = {}
        self.value = value

    def __getitem__(self, key):
        if key not in self.dic:
            self.dic[key] = DefaultDict()
        return self.dic[key]

    def __setitem__(self, key, value):
        self.dic[key] = DefaultDict(value)
        self.value = None

    def __copy__(self):
        return self.dic.copy

    def __repr__(self):
        if self.value is not None:
            return str(self.value)
        return str(self.dic)


d = DefaultDict()
d['a']['b']['c'] = 1
print(d['a']['b'])
d['a']['b']['m'] = 5
d['a']['k'] = 55
d['m'] = 34
print(d)
d['a']['b'] = d['a']['b']['m']
print(d['a']['b']['m'])
print(d)
