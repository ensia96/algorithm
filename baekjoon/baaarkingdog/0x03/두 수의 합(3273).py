_, l, x = input(), [*map(int, input().split())], int(input())

r = len(l)

print(sum(i != j and l[i] + l[j] == x for i in range(r) for j in range(r)) // 2)
