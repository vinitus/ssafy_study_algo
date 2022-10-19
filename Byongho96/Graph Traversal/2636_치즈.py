from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    global melting
    visited = [[0] * M for _ in range(N)]   # visited 배열은 반복문마다 새로 생성
    q = deque()

    visited[i][j] = 1
    q.append((i, j))

    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj] == 0:    # 0(공기)이라면, 큐에 집어넣기
                    q.append((ni, nj))
                elif arr[ni][nj] == 1:  # 1(치즈)이라면, 큐에 안집어넣고, 다음 반복문을 위해 0으로 셋팅, 녹일 치즈로 카운팅
                    arr[ni][nj] = 0
                    melting += 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time = -1
pre_melting = 1 # 직전 반복문의 melting값을 저장하기 위해 만든 변수
melting = 1     # while문 진입을 위해 1로 설정
while melting:      # 녹일치즈가 없어질때까지 반복
    time += 1
    pre_melting = melting
    melting = 0
    bfs(0, 0)       # 어차피 가장자리가 비어있으므로, (0, 0)에서 돌려주면된다

print(time)
print(pre_melting)




# def air(i, j):
#     q = deque()
#
#     arr[i][j] = 3
#     q.append((i, j))
#
#     while q:
#         i, j = q.popleft()
#         for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#             ni = i + di
#             nj = j + dj
#             if 0<= ni < N and 0<= nj < M:
#                 if not arr[ni][nj]:
#                     arr[ni][nj] = 3
#                     q.append((ni, nj))
#                 elif arr[ni][nj] == 1:
#                     arr[ni][nj] = 4
#                     melting.append((ni, nj))
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
#
# # 공기층 유입 and 녹일 치즈 선택
# ###########################################
# melting = []
# # 위, 아래
# for i in (0, N-1):
#     for j in range(M):
#         if not arr[i][j]:
#             air(i, j)
#
# # 좌, 우
# for j in (0, M-1):
#     for i in range(1, N-1):
#         if not arr[i][j]:
#             air(i, j)
#
# # print(melting)
# ###########################################
#
# # 녹일 치즈가 있으면
# cnt = 0
# N = 0
# while melting:
#     cnt += 1
#     # 치즈녹이기
#     for cheese in melting:
#         i, j = cheese[0], cheese[1]
#         arr[i][j] = 0
#
#     # 공기층 유입 and 녹일 치즈 선택
#     N = len(melting)
#     melting_copy = melting.copy()
#     melting = []
#     for cheese in melting_copy:
#         i, j = cheese[0], cheese[1]
#         if not arr[i][j]:
#             air(i, j)
#     # print(melting)
#
# print(cnt)
# print(N)
