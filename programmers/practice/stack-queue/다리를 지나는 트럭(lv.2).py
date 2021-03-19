def solution(bridge_length, weight, truck_weights):
    '''
    input
        - bridge_length : 다리의 길이 (1 <= i <= 10000)
        - weight        : 다리가 견딜 수 있는 무게 (1 <= i <= 10000)
        - truck_weights : [트럭의 무게] (1 <= [] <= 10000, 1 <= truck <= weight)
    output
        - answer        : 모든 트럭이 다리를 건너는데 걸리는 최소 시간
    result
        - 정확성 : 100/100
    '''
    time = 0
    bridge = []
    arrival = []
    on_bridge = 0

    while truck_weights:
        truck = truck_weights[0]

        if arrival and time == arrival[0]:
            on_bridge -= bridge.pop(0)
            arrival.pop(0)

        if on_bridge + truck <= weight:
            on_bridge += truck
            bridge.append(truck_weights.pop(0))
            arrival.append(time + bridge_length)

        time += 1

    return arrival[-1] + 1

print(solution(2, 10, [7, 4, 5, 6])) # 8
print(solution(100, 100, [10])) # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) # 110
