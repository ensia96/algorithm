h, m, s = map(int, input().split())
t = h*3600+m*60+s+1
print(f"{t//3600%24:02d}:{t%3600//60:02d}:{t%60:02d}")
