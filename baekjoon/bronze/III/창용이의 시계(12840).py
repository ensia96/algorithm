h, m, s = map(int, input().split())
T = 3600*h+60*m+s
for _ in ' '*int(input()):
    a, *A = map(int, input().split())
    if a == 3:
        print(T//3600 % 24, T % 3600//60, T % 60)
    else:
        T += (-1+2*(a % 2))*A[0]
        T += 86400*(T < 0)
