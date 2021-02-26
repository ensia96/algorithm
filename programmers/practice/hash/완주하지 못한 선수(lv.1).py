def solution(participant, completion):
    '''
    input
        - participant : [참가자] (1 < 100,000)
        - completion  : [완주자] (len(participant) - 1)
    output
        - answer      : 완주하지 못한 사람
    result
        - 정확성 : 80/100 (5 x)
        - 효율성 : 80/100 (5 x)
    '''
    marathon_result = dict()

    for name in participant:
        hashed = hash(name)
        if hashed not in marathon_result:
            marathon_result[hashed] = 0
        marathon_result[hashed] += 1

    for name in completion:
        hashed = hash(name)
        marathon_result[hashed] -= 1

    for name in participant:
        hashed = hash(name)
        if marathon_result[hashed] == 1:
            return name

print(solution(
    ['leo', 'kiki', 'eden'],
    ['eden', 'kiki']
)) # => 'leo'

print(solution(
    ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
    ['josipa', 'filipa', 'marina', 'nikola']
)) # => 'vinko'

print(solution(
    ['mislav', 'stanko', 'mislav', 'ana'],
    ['stanko', 'ana', 'mislav']
)) # => 'mislav'
