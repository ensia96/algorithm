A = abs
a, b, x, y = map(int, input().split())
print(min(map(A, [a-b, A(a-y)+A(b-x), A(a-x)+A(b-y)])))
