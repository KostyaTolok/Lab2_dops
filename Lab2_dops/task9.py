

def _range(start: int, end=None, step=1) -> iter:
    if end is None:
        end = start
        start = 0

    if step < 0:
        while end < start:
            yield start
            start += step
    else:
        while start < end:
            yield start
            start += step


print([i for i in _range(-5, 5, 3)])