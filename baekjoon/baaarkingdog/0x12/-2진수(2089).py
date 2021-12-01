n = int(input())

if not n:
    exit(print(0))

A = []

while n != 0:
    n, r = divmod(n, -2)
    if r < 0:
        n, r = n+1, -r
    A += str(r)

print("".join(A[::-1]))
