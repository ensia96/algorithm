i, j, k, l, m = '-|+*\n'
for t in range(int(input())):
    r, c, w, h = map(int, input().split())
    print(f"Case #{t + 1}:" + ((m + (l * w).join([j] * -~c)) * r).join(
        [m + ((i * w).join([k] * -~c))] * -~h))
