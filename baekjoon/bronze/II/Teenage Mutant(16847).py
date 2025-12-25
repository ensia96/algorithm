A = []
for t in range(int(input())):
    n, k = map(int, input().split())
    A += f"Data Set {t + 1}:\n{sum(len({A[0]} - {*A[1:]})for A in zip(*[input()for _ in '_' * -~n]))}/{k}",
print('\n\n'.join(A))
