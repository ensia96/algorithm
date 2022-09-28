n = int(input())
M = 0
for a in sorted(map(int, input().split())):
    if a > M+1:
        break
    M += a
print(M+1)
