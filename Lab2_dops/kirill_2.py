def sort_args(func):
    def wrapper(*args, **kwargs):
        arguments = sorted([*args, *kwargs.values()])
        print(f"Sorted args and kwargs: {arguments}")
        return func(*arguments)
    return wrapper


@sort_args
def f(a, b, c, d, e):
    return a + b + c + d + e


def main():
    print(f(4, 3, 12, d=6, e=1))


if __name__ == '__main__':
    main()