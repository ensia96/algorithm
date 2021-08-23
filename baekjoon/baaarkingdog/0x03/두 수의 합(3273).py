_, l, x = input(), [*map(int, input().split())], int(input())

d = {i: 1 for i in l}

print(sum(x - i in d for i in l) // 2)
