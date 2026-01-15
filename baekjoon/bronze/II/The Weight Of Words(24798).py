l, w = map(int, input().split())
print(['a' * l, 'impossible'][l * 26 < w])
