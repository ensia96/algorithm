h, m = map(int, input().split(':'))
t = h*60+m
for i in range(120):
    t += 1+(420 <= t < 600)+(900 <= t < 1140)
h, m = divmod(t, 60)
print(f'{h%24:02}:{m:02}')
