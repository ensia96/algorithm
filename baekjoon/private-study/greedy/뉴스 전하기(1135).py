def f(x): return max(
    [i+j for i, j in enumerate(sorted(f(y)for y in E[x])[::-1])]+[0])+1


n = int(input())
*A, = map(int, input().split())
E = [[]for _ in ' '*n]
for i in range(1, n):
    E[A[i]] += i,
print(f(0)-1)
