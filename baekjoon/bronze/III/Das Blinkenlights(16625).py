x, y, z = map(int, input().split())
print('yneos'[not any(not i % x and not i % y for i in range(1, z+1))::2])
