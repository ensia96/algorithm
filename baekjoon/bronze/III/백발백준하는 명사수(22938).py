a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
print('YNEOS'[(abs(a-x)**2+abs(b-y)**2) >= (c+z)**2::2])
