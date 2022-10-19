n, m = map(int, input().split())
A, B = [], []
for i in map(int, input().split()):
    if i > 0:
        A += i,
    else:
        B += i,
print(sum(a*2 for a in sorted(A)[::-m])+sum(b*-2 for b in sorted(B)[::m])
      - max(max(A+[0]), -min(B+[0])))
