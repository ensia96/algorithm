I = input
T = []
for i in range(int(I())):
    A = [I()for _ in ' ' * int(I())]
    t = f"Scenario #{i + 1}:"
    for _ in ' ' * int(I()):
        t += '\n' + ''.join(A[i]for i in [*map(int, I().split())][1:])
    T += t,
print('\n\n'.join(T))
