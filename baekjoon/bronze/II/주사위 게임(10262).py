f = lambda: sum(map(int, input().split()))
x = f() - f()
print(["Tie", "Gunnar", "Emma"][(x > 0) + 2 * (x < 0)])
