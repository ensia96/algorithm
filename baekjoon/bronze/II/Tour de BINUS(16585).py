_, R, A, B = open(0)
*R, = map(int, R.split())
a, x = A.split()
a = int(a)
b, y = B.split()
b = int(b)
print(sum([R[a - 1:], R[:a]]['l' in x]), [R[b - 1:], R[:b]]['l' in y].count(0))f
