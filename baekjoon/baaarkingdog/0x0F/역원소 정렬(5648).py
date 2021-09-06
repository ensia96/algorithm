import sys
_, *l = input().split()

while 1:
    try:
        l += input().split()
    except:
        break

print(*sorted(map(int, map(reversed, l))))
