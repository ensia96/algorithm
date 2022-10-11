for _ in ' '*int(input()):
    n, A = int(input()), sorted(map(int, input().split()))
    T, i = [0]*n, 0
    for a in A:
        T[i] = a
        i = -i-(i >= 0)
    print(max(max(T[i-1]-T[i], T[i]-T[i-1])for i in range(n)))
