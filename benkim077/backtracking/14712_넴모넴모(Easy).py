'''시간초과




from itertools import combinations
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# arr의 (i, j)위치의 포함 여부를 결정하는 함수
def dfs(arr, i, j, is_nemmo):
    global cnt, N, M

    arr[i][j] = is_nemmo

    # 가지치기
    if not is_nemmo and 1 <= i < N and 1 <= j < M:
        if arr[i - 1][j - 1] != 0 or arr[i - 1][j] != 0 or arr[i][j - 1] != 0:
            pass
        else:
            cnt += 2 ** ((M - 1 - j) + (M * (N - 1 - i)))
            return

    # 종료 조건
    if i >= N - 1 and j >= M - 1:   # arr를 모두 순회하면 종료
        return

    # 하부 함수 호출
    if j == M - 1: # 다음 행으로 넘어가야 할 때,
        dfs(arr, i + 1, 0, True) # 다음 차례가 포함되는 경우
        dfs(arr, i + 1, 0, False) # 다음 차례가 포함되지 않는 경우

    else: # 같은 행에서 오른쪽으로 이동할 때,
        dfs(arr, i, j + 1, True) # 다음 차례가 포함되는 경우
        dfs(arr, i, j + 1, False) # 다음 차례가 포함되지 않는 경우


N, M = map(int, input().split())
arr = [[False] * M for _ in range(N)]   # 게임판

temp = N * M
sm = 0  # 전체 순열의 갯수
for i in range(temp + 1):
    sm += len(list(combinations(range(temp), i)))

cnt = 0

dfs(arr, 0, 0, True)    # arr의 (0, 0)에서 True로 시작하는 경우
dfs(arr, 0, 0, False)   # arr의 (0, 0)에서 False로 시작하는 경우

print(sm - cnt)

'''
