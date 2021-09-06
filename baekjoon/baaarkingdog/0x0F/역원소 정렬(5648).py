import sys
_, *l = input().split()

while 1:
    try:
        l += input().split()
    except:
        break

print(*map(str, sorted(map(int, map(reversed, l)))))
