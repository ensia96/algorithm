A = []
for i in range(int(input())):
    n = int(input())
    A += f'Data Set {i}:\n{n+sum(1+2*(ord(c)-99)for c in input())}',
print('\n\n'.join(A))
