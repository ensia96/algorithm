*T, = map(float, input().split())
a = sum(T) / 10
print((sum((t - a)**2 for t in T) > 9) * 'NOT ' + 'COMFY')
