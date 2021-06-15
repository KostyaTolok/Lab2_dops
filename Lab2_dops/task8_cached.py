
def cached(func):
    saved = {}

    def wrapper(*args, **kwargs):
        arguments = (*args, *kwargs.values())
        keys = [key for key in saved.keys()]
        for key in keys:
            if set(arguments) == set(key):
                print("Getting saved value")
                return saved[frozenset(arguments)]
        saved[frozenset(arguments)] = func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@cached
def power(arg1, arg2):
    return arg1 ** arg2


print(power(3, 4))
print(power(3, 4))
print(power(arg2=4, arg1=3))
print(power(arg1=3, arg2=4))