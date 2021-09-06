import sys
i, m = sys.stdin.readline, 10**6+1
l = [0]*m

for _ in range(int(i())):
    l[int(i())] += 1

for i in range(m):
    for _ in range(l[i]):
        sys.stdout.write(f'{i}\n')
