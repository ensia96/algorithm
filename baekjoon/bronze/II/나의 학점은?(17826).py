*A, n = map(int, open(0).read().split())
x = sorted(A).index(n)
print(['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'F']
      [(x < 45)+(x < 35)+(x < 20)+(x < 15)+(x < 5)+(x < 2)+(x < 0)])
