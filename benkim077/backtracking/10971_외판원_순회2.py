import sys
sys.stdin = open('input.txt')

# s: 시작 지점
# v: 정점(k - 1번째 도착지)
# k + 1번째로 들르는 도시를 선택하는 함수
# cost_map: 비용 지도
# vsted: 들른 도시를 체크하는 리스트
# sm: k번째 도시까지 이동 비용
def dfs(s, v, k, cost_map, lst, vsted, sm):
    global minV

    # 가지치기
    if sm >= minV:
        return

    # 종료조건
    if k == N:
        if sm < minV:
            minV = sm
        return

    for w in lst: # k + 1번째 도시 선택(도착지)
        if k != N - 1:
            if w != s and not vsted[w]:
                if cost_map[v - 1][w - 1] == 0: # 길이 없는 경우
                    return
                vsted[w] = True
                dfs(s, w, k + 1, cost_map, lst, vsted, sm + cost_map[v - 1][w - 1])
                vsted[w] = False
        else:   # 마지막엔 무조건 s로 돌아간다.
            if cost_map[v - 1][s - 1] == 0: # 길이 없는 경우
                return
            vsted[s] = True
            dfs(s, s, k + 1, cost_map, lst, vsted, sm + cost_map[v - 1][s - 1])


N = int(input())
cost_map = [list(map(int, input().split())) for _ in range(N)]  # 비용 맵
lst = [i + 1 for i in range(N)] # 각 도시의 인덱스 리스트
vsted = [False] * (N + 1) # 도시 방문 여부 체크 리스트
minV = 1_000_000 * N

for s in lst:
    dfs(s, s, 0, cost_map, lst, vsted, 0)   # s(출발 도시)에서 다음 도시를 탐색하는 함수

print(minV)