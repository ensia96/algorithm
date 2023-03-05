w, l = int(input()), int(input())
x, y = min(w, l), max(w, l)
print(['good', 'bad'][x < 2*int(input()) or y > 2*x])
