_, *l = input().split()

while 1:
    try:
        l += input().split()
    except:
        break

print(*sorted(map(int, [i[::-1] for i in l])))
