D = [[0], [1, 0, 0], [1, 1, 0], [1, 1, 1]]
for _ in ' '*9997:
    D += [1, sum(D[-2][:2]), sum(D[-3])],
D = [*map(sum, D)]
for _ in ' '*int(input()):
    print(D[int(input())])
