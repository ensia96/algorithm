t = c = 0
for e, s in sorted([[*map(int, input().split())][::-1] for _ in '.'*int(input())]):
    if s >= t:
        t, c = e, c+1
print(c)
