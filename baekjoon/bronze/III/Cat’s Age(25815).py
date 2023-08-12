y, m = map(int, input().split())
print(*divmod([48*(y+4)+4*m, 180+9*m, 15*m][(y < 1)+(y < 2)], 12))
