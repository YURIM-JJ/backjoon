from collections import deque   

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

que = deque([(0, 0)])

while que:
    cy, cx = que.popleft()

    for dy, dx in [(0,1),(-1,0),(0,-1),(1,0)]:
        ny = cy + dy
        nx = cx + dx

        if 0<=ny<N and 0<=nx<M and arr[ny][nx] != 0:
            if arr[ny][nx] == 1:
                que.append((ny,nx))
                arr[ny][nx] = arr[cy][cx]+1
        
    if cy == N-1 and cx == M-1:
        break


print(arr[N-1][M-1])


# ================================================

from collections import deque

# N = 세로 크기(행), M = 가로 크기(열)
N, M = map(int, input().split())

# 미로 입력 받기
# 예: 101111 -> [1,0,1,1,1,1]
arr = [list(map(int, input())) for _ in range(N)]

# BFS 탐색용 큐 생성
# 시작 위치는 (0,0)
que = deque([(0, 0)])

# 큐가 빌 때까지 반복
while que:

    # 현재 위치 꺼내기
    cy, cx = que.popleft()

    # 현재 위치 기준 4방향 탐색
    # 우, 상, 좌, 하
    for dy, dx in [(0,1), (-1,0), (0,-1), (1,0)]:

        # 다음 이동 위치 계산
        ny = cy + dy
        nx = cx + dx

        # 1. 미로 범위 안에 있고
        # 2. 벽(0)이 아니어야 함
        if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] != 0:

            # 아직 방문하지 않은 길이면 (값이 1이면 처음 길)
            if arr[ny][nx] == 1:

                # 다음 탐색할 위치로 큐에 저장
                que.append((ny, nx))

                # 현재 위치 값 + 1 저장
                # 즉 시작점부터 ny,nx까지 최단거리 기록
                arr[ny][nx] = arr[cy][cx] + 1

    # 도착지에 도달했다면 종료
    # BFS 특성상 처음 도착한 값이 최단거리
    if cy == N - 1 and cx == M - 1:
        break

# 도착 지점 값 출력 = 최단거리
print(arr[N - 1][M - 1])