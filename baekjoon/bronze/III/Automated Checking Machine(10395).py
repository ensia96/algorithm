I = [*map(int, open(0).read().split())]
print('YN'[any(i != 1 for i in map(sum, zip(I[:5], I[5:])))])
