import bisect as B
n = int(input())
A = [*map(int, input().split())]
D = [0]*n
S = []
for a in A:
    i = B.bisect_left(S, a)
    if i == len(S):
        S += a,
    S[i] = min(S[i], a)
print(len(S))
