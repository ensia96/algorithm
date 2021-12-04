for _ in range(int(input())):
    n = int(input())
    R = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            R[j] = not R[j]
    print(sum(R))
