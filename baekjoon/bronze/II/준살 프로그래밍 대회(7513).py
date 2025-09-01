I = input
P = print
T = []
for i in range(int(I())):
    A = [I()for _ in ' ' * int(I())]
    P(f"Scenario #{i + 1}:")
    for _ in ' ' * int(I()):
        P(''.join(A[i]for i in [*map(int, I().split())][1:]))
