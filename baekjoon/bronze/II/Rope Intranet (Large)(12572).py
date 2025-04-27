for t in range(int(input())):
    n = int(input())
    T = [[*map(int, input().split())]for _ in ' '*n]
    print(f"Case #{t+1}:", sum((T[i][0] > T[j][0] and T[i][1] < T[j][1])+(
        T[i][0] < T[j][0] and T[i][1] > T[j][1])for i in range(n)for j in range(i+1, n)))
