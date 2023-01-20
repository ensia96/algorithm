*A, = map(int, input().split())
a, *_ = map(int, input().split())
print(+(a in A) and 1+A.index(a))
