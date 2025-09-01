I = input
P = print
T = []
for i in range(int(I())):
    P(f"Scenario #{i + 1}:")
    A = [*map(I, ' ' * int(I()))]
    for _ in ' ' * int(I()):
        P(''.join(A[int(i)]for i in I().split()[1:]))
    P()
