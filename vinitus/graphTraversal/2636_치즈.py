import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
cheeze = list(list(map(int,input().split())) for _ in range(N))
d = [(-1,0),(1,0),(0,1),(0,-1)]
answer = 0          # bfs를 실행할때마다 +1 -> bfs를 실행한 횟수 저장할 변수
cnt = 0             # 녹인 치즈의 갯수를 세어줄 녀석

def bfs():
    global answer, cnt
    answer += 1
    q = deque([])
    q.append((answer,answer))
    visited = list(list(0 for _ in range(M)) for _ in range(N))
    visited[answer][answer] = 1
    target = []
    while q:
        y,x = q.popleft()
        for dy,dx in d:
            ny = y + dy
            nx = x + dx
            if not visited[ny][nx]:
                if cheeze[ny][nx] == 1:         # 치즈를 찾으면
                    target.append((ny,nx))      # 녹일 타겟에 넣어둠
                elif cheeze[ny][nx] == 0:       # 치즈가아니면
                    q.append((ny,nx))           # 탐색할 녀석에 추가
                visited[ny][nx] = 1             # 해당 지역은 방문
    if target:                                  # 녹일 치즈가 있다면
        for y,x in target:
            cheeze[y][x] = 0                    # 녹이고
        return len(target)                      # 녹인 치즈 리스트의 길이(녹인 갯수) 반환
    else:                                       # 녹일게 없다면
        print(answer - 1)
        print(cnt)
        return 0

while True:
    cnt = bfs()
    if not cnt:
        break