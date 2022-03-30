import collections as c

for _ in ' '*int(input()):
    n, m = map(int, input().split())
    C = c.deque((j, i)for i, j in enumerate(map(int, input().split())))
    i = 1
    while C:
        if C[0][0]-max(C)[0]:
            C.rotate(-1)
        elif C.popleft()[1]-m:
            i += 1
        else:
            print(i)
            break
