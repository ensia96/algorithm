def solution(participant, completion):
    '''
    input
        - participant : [참가자] (1 < 100,000)
        - completion  : [완주자] (len(participant) - 1)
    output
        - answer      : 완주하지 못한 사람
    '''
    marathon_result = {name: False for name in participant}

    for person in completion:
        print(f'{person} : {marathon_result[person]}')
        marathon_result[person] = not marathon_result[person]
        print(f'{person} : {marathon_result[person]}')
        print('===========================')

    answer = ''
    return answer

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
