def solution(id_list, report, k):
    U = len(id_list)
    N = {id_list[i]: i for i in range(U)}
    A = [[0]*U for _ in ' '*U]
    B = [[0]*U for _ in ' '*U]

    for r in report:
        a, b = r.split()
        a, b = N[a], N[b]
        A[a][b] = B[b][a] = 1

    C = [i for i in range(U)if sum(B[i]) >= k]
    return [sum(A[i][j]for j in C)for i in range(U)]
