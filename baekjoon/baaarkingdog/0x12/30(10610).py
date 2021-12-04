n = [*map(int, input())]
print([-1, ''.join(sorted(map(str, n))[::-1])][(0 in n)*(not sum(n) % 3)])
