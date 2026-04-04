x, n = map(int, input().split())
a = 1
while (n := n - len(s := str(a))) > 0:
    a *= x
print(s[n - 1])
