a, b, c, d = sorted(map(int, input().split()))
print(min(map(abs, [d-a-b-c, d+a-b-c, d-a+b-c, d-a-b+c, d+a+b-c, d-a+b+c])))
