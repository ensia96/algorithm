*A, = map(ord, input())
print('/'.join(sorted({str(i % 2)for i in map(A.count, {*A})})))
