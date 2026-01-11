n, m = map(int, input().split())
print(*[((a := n // m + n % m), n := n - a)[0]for _ in '_' * m])
print(n)
