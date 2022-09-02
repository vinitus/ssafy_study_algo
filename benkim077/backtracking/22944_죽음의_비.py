import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

# (i, j) 좌표에서 다음 칸으로 이동하는 함수
# ans: 경로의 길이
def dfs(i, j, total, hp, um, ans):
    global arr, N, D, minV, vsted

    # 종료 조건
    if arr[i][j] == 'E':            # 목적지 도착
        if ans < minV:
            minV = ans
        return
    elif arr[i][j] == 'U':          # 우산 보충
        um = D
        um -= 1
    elif arr[i][j] == 'S':          # 시작 지점
        pass
    else:                           # '.' 비 맞는 경우
        if um > 0:
            um -= 1
        else:
            hp -= 1
    total = hp + um

    # 가지치기
    if log[i][j] < total:   # 기록된 체력 값 보다 현재 체력이 더 많으면
        log[i][j] = total       # 기록
    else:                   # 현재 체력이 더 적거나 같으면
        return                  # 그만함
    # 가지치기 2
    if total <= 0:          # 체력이 다 떨어지면 끝
        return

    # 하부 함수
    for (di, dj) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:             # 상우하좌 칸으로 이동하는 함수 호출
        ni, nj = i + di, j + dj
        if abs(ei - i) >= abs(ei - ni) or abs(ej - j) >= abs(ej - ni):  # 1 거리가 가까워지면
            if 0 <= ni < N and 0 <= nj < N and not vsted[ni][nj]:       # 2 범위 넘어가지 않고, 방문하지 않았으면
                vsted[ni][nj] = True
                dfs(ni, nj, total, hp, um, ans + 1)                         # 호출
                vsted[ni][nj] = False
    return





N, H, D = map(int, input().split())

hp, um = H, 0   # 체력, 우산 내구도
total = hp      # 전체 체력

arr = [list(input()) for _ in range(N)] # 맵

# 시작 좌표 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':    # 시작 좌표
            si, sj = i, j
        if arr[i][j] == 'E':    # 목적 좌표
            ei, ej = i, j

vsted = [[False] * N for _ in range(N)]     # 왔었는지 체크
log = [[0] * N for _ in range(N)]       # 왔었을 때 체력 기록

minV = N * N + 1                            # 최솟값 기록 변수

vsted[si][sj] = True
# print(total, hp, um)
dfs(si, sj, total, hp, um, 0)
vsted[si][sj] = False

if minV == N * N + 1:
    print(-1)
else:
    print(minV)