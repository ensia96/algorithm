s = int(input())
for i in range(s, int(input())+1):
    (s-i) % 60 or print('All positions change in year', i)
