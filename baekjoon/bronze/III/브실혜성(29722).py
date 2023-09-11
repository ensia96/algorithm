y, m, d = map(int, input().split('-'))
t = (12*y+m)*30+d+int(input())
print(f"{t//360}-{(t%360//30-(not t%30))or 12:02d}-{t%30 or 30:02d}")
