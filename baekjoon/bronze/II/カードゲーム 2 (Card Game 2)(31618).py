A = {*map(int, [*open(0)][1].split())}
print('YNeos'[not any(a + 3 in A and a + 6 in A for a in A)::2])
