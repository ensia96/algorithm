A = []
for _ in ' '*int(input()):
    a, b, c = map(int, input().split())
    A += [10000+a*1000 if a == b == c else 1000+100 *
          (a if a == b else b if b == c else c if c == a else -10+max(a, b, c))]
print(max(A))
