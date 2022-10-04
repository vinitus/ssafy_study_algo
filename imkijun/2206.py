import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("Graph/input.txt","r")
'''
1차시도 - dfs - 5%에서 시간초과

def dfs(si,sj,n):
    global min_distance

    if n >= min_distance:
        return

    if si==N and sj ==M:
        min_distance = min(min_distance, n)
        return
    
    for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
        ni, nj = si+di, sj+dj
        
        if 1<=ni<=N and 1<=nj<=M and arr[ni][nj] == '0' and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni,nj,n+1)
            visited[ni][nj] = 0
    else:
        return

N, M = map(int, input().split())

arr = [['1']* (M+2)] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1']* (M+2)]

visited = [[0]* (M+2) for _ in range(N+2)]

si, sj = 1, 1

fi, fj = N, M

min_distance = N * M

for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j] == '1':
            arr[i][j] = '0'
            dfs(si,sj,1)
            arr[i][j] = '1'
if min_distance == N*M:
    print(-1)
else:
    print(min_distance)

'''

'''
2차시도 - bfs - 5%에서 시간초과

def bfs():
    q = []
    q.append([1,1,1])
    visited = [[0]* (M+2) for _ in range(N+2)]
    visited[1][1] = 1

    while q:
        si, sj, n = q.pop(0)

        if si == N and sj == M:
            return n

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = si+di, sj+dj
        
            if 1<=ni<=N and 1<=nj<=M and arr[ni][nj] == '0' and not visited[ni][nj]:
                visited[ni][nj] = visited[si][sj] + 1
                q.append([ni,nj,n+1])

    return -1

N, M = map(int, input().split())

arr = [['1']* (M+2)] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1']* (M+2)]

visited = [[0]* (M+2) for _ in range(N+2)]

si, sj = 1, 1

fi, fj = N, M

cnts = []

for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j] == '1':
            arr[i][j] = '0'
            cnts.append(bfs())
            arr[i][j] = '1'

cnts= set(cnts)
cnts= list(cnts)

cnts = cnts[1:]

if not cnts:
    print(-1)
else:
    print(min(cnts))
'''

'''
# 3차시도 - 3차원배열 bfs
def bfs():
    q = []
    q.append([1,1,1])
    visited = [[[0,0,0] for _ in range(M+2)] for _ in range(N+2)]
    visited[1][1][1] = 1

    while q:
        si, sj, n = q.pop(0)

        if si == N and sj == M:
            return visited[si][sj][n]

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = si+di, sj+dj
        
            if 1<=ni<=N and 1<=nj<=M:
                if arr[ni][nj] == '1' and n == 1:
                    visited[ni][nj][0] = visited[si][sj][n] + 1
                    q.append([ni,nj,0])

                elif arr[ni][nj] == '0' and not visited[ni][nj][n]:
                    visited[ni][nj][n] = visited[si][sj][n] + 1
                    q.append([ni,nj,n])

    return -1

N, M = map(int, input().split())

arr = [['1']* (M+2)] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1']* (M+2)]

visited = [[0]* (M+2) for _ in range(N+2)]

print(bfs())

'''


# 4차시도 - 덱 사용
from collections import deque

def bfs():
    q = deque()
    #행, 열, 벽 부실수 있는 횟수
    q.append([1,1,1])
    #visited 배열도 3차원으로 생성
    visited = [[[0,0] for _ in range(M+2)] for _ in range(N+2)]
    #아직 안부셨으니까 
    visited[1][1][1] = 1

    while q:
        #행, 열, 벽 부실수 있는 횟수
        si, sj, n = q.popleft()

        if si == N and sj == M:
            # 최단거리 출력
            return visited[si][sj][n]

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = si+di, sj+dj
            #범위 내
            if 1<=ni<=N and 1<=nj<=M:
                #벽이 있고, 벽을 부술 수 있다면
                if arr[ni][nj] == '1' and n == 1:
                    #벽을 못부수는 상황의 visited 배열에 방문횟수 저장
                    visited[ni][nj][0] = visited[si][sj][n] + 1
                    #앞으로 벽을 못부숨
                    q.append([ni,nj,0])

                #벽을 부술 수 있던 없던, 벽이 없을 경우에
                elif arr[ni][nj] == '0' and not visited[ni][nj][n]:
                    # 벽을 부술 수 있는 횟수는 그대로 유지하면서 방문하기
                    visited[ni][nj][n] = visited[si][sj][n] + 1
                    q.append([ni,nj,n])

    #더이상 방문할 곳이 없다면 목적지에 도착이 불가능한 case
    return -1

N, M = map(int, input().split())

arr = [['1']* (M+2)] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1']* (M+2)]

visited = [[0]* (M+2) for _ in range(N+2)]

print(bfs())
