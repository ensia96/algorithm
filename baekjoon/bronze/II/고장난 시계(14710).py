h, m = map(int, input().split())
print("XO"[h % 30 * 12 == m])
