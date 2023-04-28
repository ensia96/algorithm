l, r, a = map(int, input().split())
x = min(max(l-r, r-l), a)
print(2*(min(l, r)+x)+(a-x)//2*2)
