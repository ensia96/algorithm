x, y, z = map(int, input().split())
print(*max([(i, (x-i*y)//z)
      for i in range(x//y+1)if not (x-i*y) % z] or [['Impossible']]))
