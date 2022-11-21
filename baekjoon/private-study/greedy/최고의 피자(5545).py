n = int(input())
A, B = map(int, input().split())
C = int(input())
D = sorted(int(input())for _ in ' '*n)+[0]
c, m = 0, C//A
while D:
    C += D.pop()
    t = C//(A+B*c)
    if m > t:
        break
    m = t
    c += 1
print(m)
