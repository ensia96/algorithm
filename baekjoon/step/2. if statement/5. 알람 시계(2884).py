h, m = map(int, input().split())
print(*((23 if h == 0 else h - 1, m + 15) if m < 45 else (h, m - 45)))
