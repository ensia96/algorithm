_, l, x = input(), [*map(int, input().split())], int(input())

a = [0 for _ in range(max(l) + 1)]

for i in l:
    a[i] = 1

print(sum(a[x - i] for i in l) // 2)
