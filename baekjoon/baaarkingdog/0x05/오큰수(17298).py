input()
A, C, R = [*map(int, input().split())], [], []
while A:
    a = A.pop()
    while C and C[-1] <= a:
        C.pop()
    R += [C[-1]if C else -1]
    C += a,
print(*R[::-1])
