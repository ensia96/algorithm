I = input
R = range
while (n := int(I())) > 0:
    I()
    t = 1
    for i in R(n):
        t *= i + 1
    T = [f"({i}){str(t).count(str(i)):5}"for i in R(10)]
    print(f"{n}! --\n   {'    '.join(T[:5])} \n   {'    '.join(T[5:])} ")
