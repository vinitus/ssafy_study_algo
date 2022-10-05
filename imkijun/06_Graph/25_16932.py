from re import L
import sys

sys.stdin = open("Graph/input.txt","r")

from collections import deque

'''
1차시도 - 시간초과
def bfs(i,j):
    q = deque()
    cnt = 0
    q.append([i,j])
    visited = [[0] * M for _ in range(N)]
    
    while q:
        #행, 열
        si, sj = q.popleft()

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = si+di, sj+dj
            #범위 내
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                cnt +=1
                q.append([ni,nj])

    return cnt


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_distance = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            arr[i][j] = 1
            distance = bfs(i,j)
            max_distance = max(max_distance,distance)
            arr[i][j] = 0

print(max_distance)
'''

#1로 이어져 있는 경로 그룹화 작업, cnt = 그룹의 길이
def bfs(i,j):
    cnt = 1
    q = deque()
    q.append([i,j])
    visited[i][j] = num

    while q:
        #행, 열, 
        si, sj = q.popleft()

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = si+di, sj+dj
            #범위 내
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == 1 and not visited[ni][nj]:
                    #
                    visited[ni][nj] = num
                    q.append([ni,nj])
                    cnt +=1
    return cnt


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

# 그룹화 - 2번그룹, 3번그룹, 4번그룹, ....
num = 2
group = {}

zeros = [] #1로 바꿀 후보 담을 리스트 선언

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i,j)
            #num번 그룹은 cnt만큼의 길이를 가지고 있다.
            group[num] = cnt
            num +=1

        if arr[i][j] == 0:
            zeros.append([i,j])

#중간점검
# print(group)
# for val in visited:
#     print(val)

#최장거리 찾는 변수 선언
max_distance = 0

for ci, cj in zeros:
    temp = []
    #상하좌우에 위치한 그룹 찾기
    for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<M:
            if arr[ni][nj] == 1 and visited[ni][nj] not in temp:
                temp.append(visited[ni][nj])
    
    #현재위치를 포함한 전체 길이 카운트 변수 선언
    distance = 1

    #그룹의 길이 더하기
    for val in temp:
        distance += group[val]

    max_distance = max(max_distance,distance)

print(max_distance)