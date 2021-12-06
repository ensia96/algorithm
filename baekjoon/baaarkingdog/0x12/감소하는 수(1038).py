l = []


def solve(A):
    if A//10**9:
        return
    l.append(A)
    for i in range(A % 10):
        solve(A*10+i)


for i in range(10):
    solve(i)
l.sort()
n = int(input())
print(-(len(l) <= n) or l[n])
