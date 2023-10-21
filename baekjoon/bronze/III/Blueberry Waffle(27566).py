r, f = map(int, input().split())
print(['down', 'up'][round(180/r*f/360) % 2])
