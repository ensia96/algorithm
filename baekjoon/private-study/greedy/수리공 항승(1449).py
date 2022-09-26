n, l = map(int, input().split())
A = sorted(map(int, input().split()))
c = 0
while A:
    x = A.pop()
    while A and A[-1] > x-l:
        A.pop()
    c += 1
print(c)
