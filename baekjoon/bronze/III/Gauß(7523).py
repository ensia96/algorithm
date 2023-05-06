A = []
for i in range(int(input())):
    n, m = map(int, input().split())
    A += f"Scenario #{i+1}:\n{(n+m)*(m-n+1)//2}",
print('\n\n'.join(A))
