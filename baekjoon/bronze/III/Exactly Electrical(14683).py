a, b, c, d, e = map(int, open(0).read().split())
x = abs(a-c)+abs(b-d)
print('NY'[x == e or (x <= e and (e-(a+b)) % 2 == 0)])
