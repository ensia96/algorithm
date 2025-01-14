H, T, X = "HT "
while (A := input()) != "# #":
    a, b = A.split()
    n = int(input())
    print(a, x := sum(eval(input().replace(X, "==")) for _ in X * n), b, n - x)
