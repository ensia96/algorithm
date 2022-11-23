n = int(input())
S = C = 0
for i in map(int, input().split()):
    S += i
    C += i//2
print("YES" if not S % 3 and C >= S//3 else"NO")
