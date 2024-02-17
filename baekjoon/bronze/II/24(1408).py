f, m = lambda: map(int, input().split(':')), 60
a, b, c = f()
x, y, z = f()
T = (x*m+y)*m+z-(a*m+b)*m-c
T += 24*m*m*(T < 0)
print(f"{T//3600:02d}:{T%3600//m:02d}:{T%m:02d}")
