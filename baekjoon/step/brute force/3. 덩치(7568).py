l = {tuple(map(int, input().split())): 1 for _ in range(int(input()))}

for a in l:
    for b in l:
        if a == b:
            continue
        h, i = a
        j, k = b
        if h < j and i < k:
            l[a] += 1

print(*l.values())
