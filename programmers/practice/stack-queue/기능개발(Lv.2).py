def solution(progresses, speeds):
    '''
    input
        - progresses : [작업 진도] ([] <= 100, 1 <= i < 100)
        - speeds     : [작업 속도] ([] <= 100, 1 <= i <= 100)
    output
        - answer     : [한 번에 배포된 작업의 수]
    '''
    answer = []
    time   = 0

    while progresses:
        time = (100 - progresses.pop(0)) / speeds.pop(0)
        answer.append(1)

    return answer

print(solution(
    [93, 30, 55],
    [1, 30, 5])) # [2, 1]
print(solution(
    [95, 90, 99, 99, 80, 99],
    [1, 1, 1, 1, 1, 1])) # [1, 3, 2]
