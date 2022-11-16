n = int(input())
A = input()
print(min(A.rstrip('B').count('B'), A.rstrip('R').count('R'),
      A.lstrip('B').count('B'), A.lstrip('R').count('R')))

# O(n) 으로 풀어야하는 건 알겠는데 어떻게 풀지 감이 안 옴..
# -> 같은 색이 나란히 있는 구간의 크기와 수를 활용하면 될 듯?
# -> 질문 게시판에도 힌트가 없어서 그냥 검색해서 품..
# -> 어느 방향으로 어떤 색을 모을지를 생각했어야 했음..
# -> 한번에 1개씩만 움직일 수 있다는 게 핵심이었음
