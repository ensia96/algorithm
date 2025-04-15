def solution(today, terms, privacies):
    X, Y, Z = map(int, today.split('.'))
    A = []
    D = {}
    for t in terms:
        x, y = t.split()
        D[x] = int(y)
    for i in range(len(privacies)):
        p = privacies[i]
        x, y = p.split()
        a, b, c = map(int, x.split('.'))
        c -= 1
        d, b = divmod(b+D[y], 12)
        a += d
        if c == 0:
            c += 28
            b -= 1
        if b == 0:
            b += 12
            a -= 1
        if a > X:
            continue
        if a == X and b > Y:
            continue
        if a == X and b == Y and c >= Z:
            continue
        A += i+1,
    return A


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], [
      "2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))

# [1, 3]

print(solution("2020.01.01", ["Z 3", "D 5"], [
      "2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

# [1, 4, 5]

# 모든 달이 28일임
# -> 약관 날짜만큼 더한 다음에 오늘 날짜와 비교
# -> 왜 틀리는지 모르겠음;
# -> 연월일 변환에서 싦수함..
