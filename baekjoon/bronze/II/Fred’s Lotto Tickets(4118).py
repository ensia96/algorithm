while (n := int(input())) > 0:
    T = []
    for _ in " " * n:
        T.extend(map(int, input().split()))
    print("YNeos"[set(T) != {*range(1, 50)} :: 2])
