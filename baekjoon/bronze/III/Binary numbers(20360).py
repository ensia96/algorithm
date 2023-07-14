print(*[i for i, j in enumerate(bin(int(input()))[:1:-1])if j == '1'])
