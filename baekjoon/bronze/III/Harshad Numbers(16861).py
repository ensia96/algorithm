A = input()
while 1:
    n, m = int(A), sum(map(int, A))
    n % m or exit(print(n))
    A = str(n+1)
