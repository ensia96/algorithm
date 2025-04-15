# 인원수만큼 인접한 객실을 배정해야함
# 객실 이용률을 목표치 이상으로 만들어야 함
# 예약을 거절할 수도 있음
# 예약 거절을 최소화하면서 객실 이용률을 높여야 함

# 건물 크기 = h * w
# 객실마다 고유한 객실 번호가 있음 => (객실의 층)(객실의 위치)
# 2층 31번째 객실 = 2031, 10층 75번째 객실 = 10075
# -> 함수화하는 게 좋을 듯

# 체크아웃 이후 바로 체크인 가능

# 예약 요청 정보 : id, 객실 수, 체크인 날짜, 체크아웃 날짜
# x = 요청 날짜 일 때, x + 1 <= 체크인 날짜 <= x + 21

# 예약 답변 기한까지 승낙, 거절 여부를 정해야 함
# 답변 기한 = min(요청 날짜 + 14, 체크인 날짜 - 1)
# 답변 안하면 거절로 처리됨 -> 가능하면 무조건 승낙해야 함

# 인접한 객실 = 같은 층의 연속된 객실

# 시나리오 1
# - h = 3, w = 20
# - 1 <= 날짜 <= 200
# - 요청 빈도    : 평균 1일 1건
# - 요청 객실 수 : 1 ~ 10
# - 머무는 기간  : 1 ~ 20
# - 객실 이용률 목표치 = 60%

# 시나리오 2
# - h = 10, w = 200
# - 1 <= 날짜 <= 1000
# - 요청 빈도    : 평균 1일 4건
# - 요청 객실 수 : 1 ~ 50
# - 머무는 기간  : 1 ~ 100
# - 객실 이용률 목표치 = 75%
# - 추가 : 성수기가 60일씩 2번 있음

# 최대한 빠르게 답변해야 함
# 객실 수가 많은 곳부터 처리하는게 유리함
# 승낙했으나 실패하는 경우를 최소화해야 함
# 요청 거절도 최소화해야 함

# 1. 요청 관련 함수 구현 (v)
# 2. 입력 확인 + 아이디어 정리 (v)
# 3. 구현 후 제출 (v)

# - 1번 시나리오 대응 후, 2번 시나리오에서 반복

# 최대한 많은 경우의 수를 고려하기 위해 요청이 자동으로 거절되기 전까지 최대한 많은 예약을 확인
# 방은 최대한 앞쪽부터 배정

# 빈 공간 찾기 + 주변 방의 체크아웃 날짜 확인
# 단편화를 최대한 막아야 함
# 가장 딱 맞는 공간
# 1. 주변 방의 체크 아웃 날짜가 큰 -> 단편화 가능성을 줄일 수 있음
# 2. 주변 방의 체크 아웃 날짜가 작은 -> 단편화 기간을 최소화할 수 있음
# 1, 2 기준은 바꿔볼만한 듯


from request import start, get_reservations, reply, simulate, get_score
from heapq import heappush as push, heappop as pop, heapify

h = w = hotel = day = 0


def get_deadline(cin):
    return min(day+14, cin-1)


def generate_room_number(y, x):
    return str(y)+str(x).zfill(3)


def check_empty_space(cin, count):
    for i in range(h):
        c = 0
        for j in range(w):
            if hotel[i][j] <= cin:
                c += 1
            else:
                c = 0
            if c == count:
                return i, j-count+1


# def test(scenario):
#     global h, w, hotel, day
#
#     start(scenario)
#     heap = []
#     done = []
#
#     if scenario == 1:
#         h, w, days = 3, 20, 201
#     else:
#         h, w, days = 10, 200, 1001
#
#     hotel = [w*[0]for _ in range(h)]
#
#     while day < days:
#         reservations = get_reservations()
#         assignment = []
#
#         print(day)
#         # print('reservations : ', reservations)
#
#         for reservation in reservations:
#             rid = reservation['id']
#             count = reservation['amount']
#             cin = reservation['check_in_date']
#             cout = reservation['check_out_date']
#
#             deadline = get_deadline(cin)
#             push(heap, (deadline, count, cin, cout, rid))
#
#         while heap:
#             deadline, count, cin, cout, rid = heap.pop()
#
#             A = check_empty_space(count)
#             if A:
#                 i, j = A
#                 room_number = generate_room_number(i+1, j+1)
#                 assignment += {'id': rid, 'reply': 'accepted'},
#                 push(done, (cin, rid, room_number))
#                 for x in range(j, j+count):
#                     hotel[i][x] = cout
#             elif day < deadline:
#                 push(heap, (deadline, count, cin, cout, rid))
#                 break
#
#         if assignment:
#             # print('reply : ', assignment)
#             reply(assignment)
#
#         assignment = []
#         while done and done[0][0] <= day:
#             cin, rid, room_number = pop(done)
#             if cin == day:
#                 assignment += {'id': rid, 'room_number': room_number},
#
#         # print('simulate : ', assignment)
#         result = simulate(assignment)
#         print(result)
#         day = result['day']
#
#         for i in range(h):
#             for j in range(w):
#                 if hotel[i][j] <= day:
#                     hotel[i][j] = 0
#         get_score()
#     simulate([])


def test(scenario):
    global h, w, hotel, day
    day = start(scenario)
    heap = []
    done = []

    # 호탤 행렬 <- 체크 아웃 날짜를 기록
    # 아직 답변 기한이 지나지 않은 예약 목록 <- 우선 순위 큐로 구현
    # 방 배정 목록 <- 우선 순위 큐로 구현

    if scenario == 1:
        h, w, days = 3, 20, 201
    else:
        h, w, days = 10, 200, 1001

    hotel = [w*[0]for _ in range(h)]

    while day < days:
        # 예약 확인
        reservations = get_reservations()
        assignment = []
        temp = []

        # 우선순위
        # 1. 답변 기한이 얼마 안 남은
        # 2. 체크인 기한이 얼마 안 남은
        # 3. 많은 공간을 필요로 하는
        # 4. 짧게 머무는
        # 3, 4 순서는 바꿔봐도 괜찮을 듯
        for reservation in reservations:
            rid = reservation['id']
            count = reservation['amount']
            cin = reservation['check_in_date']
            cout = reservation['check_out_date']

            deadline = get_deadline(cin)
            stay = cout-cin

            push(heap, (deadline, cin, -count, stay, rid, cout))

        # 힙 확인
        # 가장 이른 답변 기한까지 5일 남았을 때까지는 대기
        while heap:
            deadline, cin, count, stay, rid, cout = pop(heap)

            possible_spaces = check_empty_space(cin, -count)

            if possible_spaces:
                i, j = possible_spaces
                position = generate_room_number(i+1, j+1)

                for x in range(j, j-count):
                    hotel[i][x] = cout

                assignment += {'id': rid, 'reply': 'accepted'},
                push(done, (cin, rid, position))

            elif day < deadline:
                push(temp, (deadline, cin, count, stay, rid, cout))

        while temp:
            push(heap, pop(temp))

        # 요청에 대한 결과 응답 + 방 배정 목록 갱신 + 호텔 정보 갱신
        if assignment:
            reply(assignment)

        assignment = []
        # 실제 방 배정 + 하루 지나감
        while done and done[0][0] <= day:
            cin, rid, position = pop(done)
            if day == cin:
                assignment += {'id': rid, 'room_number': position},

        result = simulate(assignment)
        print(result)
        day = result['day']
        get_score()


test(int(input('시나리오 번호 : ')))

371.2645167889119 + 482.5598313188017 = 853.8243481077136
