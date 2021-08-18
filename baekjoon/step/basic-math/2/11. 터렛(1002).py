def check():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    l = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    s, d = r1 + r2, abs(r1 - r2)

    if l == 0:
        if r1 == r2:
            return -1
        return 0

    if s < l or l < d:
        return 0

    if s == l or d == l:
        return 1

    if d < l < s:
        return 2


for _ in range(int(input())):
    print(check())

# 두 원의 위치 관계 참고 글 : https://mathbang.net/101
# 파이썬 절대값 참고 글 : https://blockdmask.tistory.com/380
