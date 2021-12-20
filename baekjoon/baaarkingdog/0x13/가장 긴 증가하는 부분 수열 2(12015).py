import bisect as B
n = int(input())
i, *A = map(int, input().split())
T = [i]
for a in A:
    if T[-1] < a:
        T += [a]
    else:
        T[B.bisect_left(T, a)] = a
print(len(T))
