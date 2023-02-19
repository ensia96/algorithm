x, y = float(input()), float(input())
z = x//y**2
print(['Normal ', 'Under', 'Over'][2*(z > 25)+(z < 18.5)]+'weight')
