class Vector:

    def __init__(self, *args):
        if not args:
            self.values = []
        else:
            self.values = [*args]

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return Vector(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def __add__(self, other):
        res = self.values.copy()

        if len(other) != len(self.values) or not isinstance(other, Vector):
            raise ValueError

        for i in range(len(self.values)):
            res[i] += other[i]

        return res

    def __sub__(self, other):
        res = self.values.copy()

        if len(other) != len(self.values) or not isinstance(other, Vector):
            raise ValueError

        for i in range(len(self.values)):
            res[i] -= other[i]

        return res

    def __mul__(self, other):
        res = self.values.copy()

        if not isinstance(other, int) or not isinstance(other, float):
            raise ValueError

        for i in range(len(self.values)):
            res[i] *= other

        return res

    def scalar_mul(self, other):
        res = 0

        if not isinstance(other, Vector) or len(self.values) != len(other):
            raise ValueError

        for i in range(len(self.values)):
            res += other[i] * self.values[i]

        return res

    def __eq__(self, other):

        if not isinstance(other, Vector):
            raise ValueError

        if len(self.values) != len(other):
            return False

        for i in range(len(self.values)):
            if self.values[i] == other[i]:
                continue
            else:
                return False

        return True


v = Vector(1, 2, 3, 4, 6)
v3 = Vector(1, 2, 3, 4, 1)
for val in v:
    print(val)
print(v + v3)
