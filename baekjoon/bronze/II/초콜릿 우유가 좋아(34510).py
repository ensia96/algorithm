a, b, c = map(int, input().split())
print(sum(c + [a + b, -a][i % 2]for i in range(int(input()))))
