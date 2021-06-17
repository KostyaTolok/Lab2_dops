a = [i for i in range(10) if i % 2]
print(a)

print(eval("1 + 6"))

a = lambda x: x ** 2
print(a(2))

print(5 ** 2 + 16 // 2 * (2 + 2))

a = [1, 2, 3]
b = a + [1, 2, 3, 4]
c = list(set(b))
print(c)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = arr[::-1]
print(arr)

d = dict([
    ("Ann", 23),
    ("DDD", 33)
])
print(d)

a = [1, 2, 3, 4]
b = [2, 3, 4, 5, 6]
c = [i for i in a for j in b if i == j]
print(c)

c = filter(lambda x: x < 3, a)
print(c)


def gen():
    return 4, 5, 2, 2, 2


def foo(a, b, c=7, *args):
    return a + b + c


print(foo(*gen()))

a = [1, 2]

try:
    b = a[5]
except IndexError:
    print("index")
finally:
    print("bye")


class A:
    def read(self):
        print("A")


class B:
    def read(self):
        print("B")


class User(A, B):
    def read(self):
        super().read()
        print("USER")


u = User()
u.read()

print(isinstance(u.read, type))


def closure():
    x = "A"

    def _closure():
        nonlocal x
        x += "B"
        return x

    return _closure()


f = closure
print(f())
print(f())
print(f())


class Meta(type):
    def __new__(cls, name, bases, namespace):
        x = super().__new__(cls, name, bases, namespace)
        x.attr = int(name.split('_')[-1])
        return x


class Foo_100(metaclass=Meta):
    pass


class Bar_200(metaclass=Meta):
    pass


print(Foo_100.attr, Foo_100().attr, Bar_200.attr)


def bar(d=[]):
    d.append(len(d))
    print(d)


bar()
bar([])
bar()

ar = ['a', 'b', 'c']
a = zip(range(len(ar)), ar)
a = list(a)

b = list(enumerate(ar))
print(a == b)


def my_gen():
    _sum = 0
    for i in range(5):
        _sum += 1
        yield _sum


gen = my_gen()

for i in range(10):
    next(my_gen())

print(next(my_gen()))


class Base:
    def foo(self):
        raise NotImplemented

class Simple(Base):
    def foo(self):
        print("simple")

class Complex(Simple):
    def foo(self):
        print("complex")

Complex().foo()