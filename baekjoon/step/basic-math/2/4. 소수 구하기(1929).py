m, n = map(int, input().split())
x = {2}

for i in range(m, n + 1):
    a = 1

    for y in x:
        if not i % y:
            x.add(i)
            a = 0
            print(x)
            break

    if not a:
        continue

    for j in range(2, int(i ** 0.5)):
        if not i % j:
            a = 0
            break
    if a:
        x.add(i)
        print(i)

# 에라토스테네스의 체 풀이 관련 글 : https://leejunggae.tistory.com/3
