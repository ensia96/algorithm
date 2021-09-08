n, k = map(int, input().split())
c, a = [int(input()) for _ in range(n)], 0

while k > 0 and c:
    i = c.pop()
    if i <= k:
        a += k//i
        k %= i

print(a)
