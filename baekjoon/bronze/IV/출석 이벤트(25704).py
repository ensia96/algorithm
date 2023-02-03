n, p = int(input())//5, int(input())
A = [(500, 1), (p//10, 2), (2000, 3), (p//4, 4)]
while n:
    x, y = max(A[:n])
    p = max(p-x, 0)
    n = max(n-y, 0)
print(p)
