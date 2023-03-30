A = []
for _ in ' '*int(input()):
    n = int(input())
    A += '\n'.join(f"#{'#J'[0<i%n<n-1]*(n-2)}{'#'*(n>1)}"for i in range(n)),
print('\n\n'.join(A))
