k, d, a = map(int, input().split('/'))
print(['go', 'ha'][k+a < d or not d]+'su')
