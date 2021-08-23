_, l, x = input(), [*map(int, input().split())], int(input())

print(sum(x - l[i] in l for i in range(len(l))) // 2)
