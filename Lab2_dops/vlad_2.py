class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "({}, {})".format(self.left, self.right)


def main():
    intervals = []
    intervals.append(Interval(6, 9))
    intervals.append(Interval(1, 3))
    new_interval = Interval(2, 5)
    print("Start: ")
    for elem in intervals:
        print(elem, end=" ")
    print()
    print("New interval", new_interval)

    task(intervals, new_interval)

    print("End:")
    for elem in intervals:
        print(elem, end=" ")
    print()

    intervals.clear()
    intervals.append(Interval(5, 6))
    intervals.append(Interval(7, 8))
    intervals.append(Interval(1, 2))
    intervals.append(Interval(10, 11))
    intervals.append(Interval(12, 16))
    new_interval = Interval(4, 11)
    print("Start: ")
    for elem in intervals:
        print(elem, end=" ")
    print()
    print("New interval", new_interval)
    task(intervals, new_interval)
    print("End:")
    for elem in intervals:
        print(elem, end=" ")
    print()


def task(intervals, new_interval):
    left_intervals = find_interval(intervals, new_interval.left)
    right_intervals = find_interval(intervals, new_interval.right)

    if len(left_intervals) != 0:
        new_interval.left = min([interval.left for interval in left_intervals])
        for interval in left_intervals:
            intervals.remove(interval)

    if len(right_intervals) != 0:
        new_interval.right = max([interval.right for interval in right_intervals])
        for interval in right_intervals:
            intervals.remove(interval)

    inner = find_inner(intervals, new_interval.left, new_interval.right)

    if len(inner) != 0:
        for interval in inner:
            intervals.remove(interval)

    intervals.append(new_interval)


def find_interval(intervals, value):
    res = []
    for elem in intervals:
        if elem.left <= value <= elem.right:
            res.append(elem)
    return res


def find_inner(intervals, left, right):
    res = []
    for elem in intervals:
        if left < elem.left and right > elem.right:
            res.append(elem)
    return res


if __name__ == "__main__":
    main()
