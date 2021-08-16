for _ in range(int(input())):
    k, n = int(input()), int(input())
    a = [i + 1 for i in range(n)]
    for i in range(k):
        a = [sum(a[: i + 1]) for i in range(n)]
    print(a.pop())
