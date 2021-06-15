
def fibonacci(end):
    if end < 2:
        raise ValueError
    first_num = 0
    yield first_num
    second_num = 1
    yield second_num
    for i in range(2, end):
        num = first_num + second_num
        yield num
        first_num = second_num
        second_num = num


print([val for val in fibonacci(10)])