l, r = map(int, input().split())
m = max(l, r)
print('EOvdedn'[l != r::2]+f" {m*2}"if m else 'Not a moose')
