def permutations(items):
    if len(items) == 0:
        yield []
    else:
        pi = items[:]
        for i in range(len(pi)):
            pi[0], pi[i] = pi[i], pi[0]
            for p in permutations(pi[1:]):
                yield [pi[0]] + p


a = [1, 3, 4, 2, 23]
for i in permutations(a):
    print(i)

