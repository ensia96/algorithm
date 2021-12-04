n = ''.join(sorted(input())[::-1])
print([-1, n][not int(n) % 30])
