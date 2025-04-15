m = 50
M = m**2
T = M*['']
D = [{i}for i in range(M)]


def get_index(x, y):
    return (int(x)-1)*50+(int(y)-1)


def update(A):
    if len(A) == 2:
        for i in range(M):
            if T[i] == A[0]:
                T[i] = A[1]
    else:
        t = get_index(A[0], A[1])
        for i in D[t]:
            T[i] = A[2]


def merge(A):
    x = get_index(A[0], A[1])
    y = get_index(A[2], A[3])
    for i in [*D[x]]:
        D[i] |= D[y]
    for i in [*D[y]]:
        D[i] |= D[x]
    if T[x]:
        update([A[0], A[1], T[x]])
    elif T[y]:
        update([A[2], A[3], T[y]])


def unmerge(A):
    t = get_index(A[0], A[1])
    x = T[t]
    for i in D[t]:
        T[i] = ''
        D[i] = {i}
    if x:
        T[t] = x


def solution(commands):
    R = []
    for C in commands:
        c, *A = C.split()
        if c == 'UPDATE':
            update(A)
        elif c == 'MERGE':
            merge(A)
        elif c == 'UNMERGE':
            unmerge(A)
        else:
            t = get_index(A[0], A[1])
            if T[t]:
                R += T[t],
            else:
                R += 'EMPTY',
    return R


print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
      "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# ["EMPTY", "group"]

T = M*['']
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d",
      "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
# ["d", "EMPTY"]

# 그냥 구현 문제인듯?
# -> 복잡하게 생각하기 싫어서 병합 여부는 집합에 대한 배열로 저장
# -> 그냥 딱 설명대로만 구현함
# -> 병합, 병합 해제를 구현할 때 조금 헤맴 (서로소 집합 활용해보려 함)
