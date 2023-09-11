y, m, d = map(int, input().split('-'))
t = 360*y+30*m+d+int(input())
print(f'{(t-31)//360}-{~-t%360//30 or 12:02d}-{t%30 or 30:02d}')
