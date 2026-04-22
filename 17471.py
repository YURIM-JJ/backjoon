# ㅓㅣㅏㄴㄹ알일아ㅣㄱ 으아아아아아아아아악

from collections import deque

def bfs(lst):
    q = deque()
    visited = set()

    q.append(lst[0])
    visited.add(lst[0])

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if nxt in lst and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    return len(visited) == len(lst)


def recur(idx, A_lst, B_lst):
    global min_diff

    if idx == N:
        if len(A_lst) == 0 or len(B_lst) == 0:
            return
        # a와 b의 인구 차이의 최솟값 구하기 
        if bfs(A_lst) and bfs(B_lst) : 

            a_sum = 0
            b_sum = 0

            for a in A_lst:
                a_sum += people[a]

            for b in B_lst:
                b_sum += people[b]

            diff =  abs(a_sum - b_sum)

            if min_diff > diff:
                min_diff = diff

        return min_diff
    
    recur(idx+1, A_lst+[idx], B_lst)
    recur(idx+1, A_lst, B_lst+[idx])



N = int(input())
people = list(map(int, input().split()))

graph =[[] for _ in range(N)]

for i in range(N):
    data = list(map(int, input().split()))

    for x in data[1:]:
        graph[i].append(x-1)

min_diff = 9999
recur(0, [], [])


if min_diff == 9999:
    print(-1)
else:
    print(min_diff)

# =================================================

from collections import deque


# lst 그룹이 서로 연결되어 있는지 확인하는 BFS 함수
def bfs(lst):
    # BFS 탐색용 큐
    q = deque()

    # 방문한 구역 저장 (중복 방문 방지)
    visited = set()

    # lst의 첫 번째 구역을 시작점으로 큐에 넣기
    q.append(lst[0])

    # 시작점 방문 처리
    visited.add(lst[0])

    # 큐가 빌 때까지 반복
    while q:
        # 현재 탐색할 구역 꺼내기
        now = q.popleft()

        # 현재 구역과 연결된 다른 구역들 확인
        for nxt in graph[now]:

            # nxt가 같은 그룹(lst)에 속해 있고
            # 아직 방문하지 않았다면
            if nxt in lst and nxt not in visited:

                # 방문 처리
                visited.add(nxt)

                # 다음 탐색 대상으로 큐에 넣기
                q.append(nxt)

    # 방문한 구역 수 == 그룹 크기
    # 즉 그룹 전체를 다 방문했으면 연결된 상태
    return len(visited) == len(lst)


# 모든 구역을 A 선거구 / B 선거구로 나누는 재귀 함수
def recur(idx, A_lst, B_lst):
    global min_diff

    # idx == N 이면 모든 구역 배정 완료
    if idx == N:

        # 한쪽 선거구가 비어있으면 불가능
        if len(A_lst) == 0 or len(B_lst) == 0:
            return

        # A와 B가 둘 다 연결되어 있어야만 가능
        if bfs(A_lst) and bfs(B_lst):

            # A 선거구 인구 합
            a_sum = 0

            # B 선거구 인구 합
            b_sum = 0

            # A 선거구 인구수 합산
            for a in A_lst:
                a_sum += people[a]

            # B 선거구 인구수 합산
            for b in B_lst:
                b_sum += people[b]

            # 두 선거구 인구 차이 절댓값
            diff = abs(a_sum - b_sum)

            # 최소값 갱신
            if min_diff > diff:
                min_diff = diff

        return

    # 현재 idx번 구역을 A 선거구에 넣는 경우
    recur(idx + 1, A_lst + [idx], B_lst)

    # 현재 idx번 구역을 B 선거구에 넣는 경우
    recur(idx + 1, A_lst, B_lst + [idx])


# ---------------- 입력 ----------------

# 구역 개수
N = int(input())

# 각 구역 인구수
people = list(map(int, input().split()))

# 그래프 생성
graph = [[] for _ in range(N)]

# 각 구역 연결 정보 입력
for i in range(N):
    data = list(map(int, input().split()))

    # data[0] = 연결된 구역 수 (사용 안 함)
    # data[1:] = 실제 연결된 구역 번호들
    for x in data[1:]:

        # 문제 번호는 1번부터 시작하므로
        # 파이썬 인덱스 맞추려고 -1
        graph[i].append(x - 1)


# 최소 인구 차이 (초기값 크게 설정)
min_diff = 9999

# 0번 구역부터 시작해서 모든 경우 탐색
recur(0, [], [])


# 끝까지 갱신 안 되었으면 가능한 선거구 분할이 없는 것
if min_diff == 9999:
    print(-1)
else:
    print(min_diff)