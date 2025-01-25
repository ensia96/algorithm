a, b = map(int, input().split())
A = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
x, y = divmod(b, 26)
print("SN", str(a) + [A[y], (A[x % 26 - (not y)] + A[y]).lower()][b > 26])
