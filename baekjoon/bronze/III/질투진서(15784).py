a, *A = open(0)
_, a, b = map(int, a.split())
B = [l.split()[b-1]for l in A]
print('HAANPGPRY'[int(B[a-1]) < max(map(int, A[a-1].split()+B))::2])
