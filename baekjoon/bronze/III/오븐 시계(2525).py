a, b = map(int, input().split())
a, b = divmod(a*60+b+int(input()), 60)
print(a % 24, b)
