l, _ = lambda: map(int, input().split()), 0
_ = l()
print(*sorted([*l(), *l()]))
