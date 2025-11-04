I = input
while (n := int(I())) > 0:
    I()
    t = 1
    for i in range(n):
        t *= i + 1
    T = [f"({i}){str(t).count(i):5}"for i in '0123456789']
    print(f"{n}! --\n   {'    '.join(T[:5])} \n   {'    '.join(T[5:])} ")
