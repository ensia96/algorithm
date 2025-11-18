A = {*map(int, [*open(0)][1].split())}
print('YNeos'[all({a + 3, a + 6} - A for a in A)::2])
