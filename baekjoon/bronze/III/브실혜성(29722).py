y, m, d = map(int, input().split('-'))
t = (12*y+m)*30+d+int(input())
print(f"{t//360:04d}-{t%360//30:02d}-{t%30:02d}")
