f = lambda: map(int, input().split())
n, q = f()
B = [0] * -~n
for l in range(q):
    a, b, c = f()
    B[b] += c * (a < 2)
    a > 1 and print(sum(B[b : c + 1]))
