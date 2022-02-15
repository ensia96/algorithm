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

# 신입 공채 당시에 제출했던 코드
#
# def solution(id_list, report, k):
#     user_data = {user: {'reported from': set(), 'reported': set()}
#                  for user in id_list}
#
#     for user, reported in map(lambda x: x.split(), report):
#         user_data[user]['reported'].add(reported)
#         user_data[reported]['reported from'].add(user)
#
#     suspended_users = [
#         *filter(lambda x: len(user_data[x]['reported from']) >= k, user_data)]
#
#     return [len([*filter(lambda x: x in suspended_users, user_data[user]['reported'])])
#             for user in id_list]
