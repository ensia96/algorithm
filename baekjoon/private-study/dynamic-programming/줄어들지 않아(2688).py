D = [[1]*10]
for _ in ' '*63:
    D += [sum(D[-1][:i+1])for i in range(10)],
D = [*map(sum, D)]
for _ in ' '*int(input()):
    print(D[int(input())-1])
