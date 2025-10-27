I, S = input, sum
while S(A := [*map(int, input().split())]):
    n, m = A
    A, B = [int(I())for _ in " " * n], [int(I())for _ in " " * m]
    x, y = S(A), S(B)
    T = [(a, b)for a in A for b in B if x - a + b == y - b + a]
    print(*[(-1), min(T, key=S)][len(T) > 0])
