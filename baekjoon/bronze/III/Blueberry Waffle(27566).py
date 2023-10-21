r, f = map(int, input().split())
print(['up', 'down'][90 <= 180*f/r % 360 <= 270])
