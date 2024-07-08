a, b = map(int, input().split())
for i in range(max(a, b)):
    a % -~i + b % -~i < 1 and print(-~i, a // -~i, b // -~i)
