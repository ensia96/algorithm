l = [0 for _ in range(10)]

for c in input():
    l[int(c)] += 1

n, o = l[6], l[9]
l[6], l[9] = (n + o) // 2 + (n + o) % 2, 0

print(max(l))
