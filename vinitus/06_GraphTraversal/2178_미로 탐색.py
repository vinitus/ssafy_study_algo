import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
lst = [[0] * (M+2)]
for _ in range(N):
    lst.append([0] + list(map(int,input())) + [0])
lst.append([0] * (M+2))
d = [(-1,0),(1,0),(0,-1),(0,1)]

answer = N*M

def bfs():
    global answer
    arr = list(list(0 for _ in range(M+2)) for _ in range(N+2))
    arr[1][1] = 1
    y,x = 1,1
    q = deque([(1,1,1)])
    while q:
        y,x,cnt = q.popleft()
        if (y,x) == (N,M):
            answer = min(answer, cnt)
        for dy,dx in d:
            if lst[y+dy][x+dx] == 1:
                if not arr[y+dy][x+dx]:
                    q.append((y+dy,x+dx,cnt+1))
                    arr[y+dy][x+dx] = cnt + 1
                else:
                    if arr[y+dy][x+dx] > cnt + 1:
                        arr[y+dy][x+dx] = cnt + 1
                        q.append((y,x,cnt+1))
                        
bfs()

print(answer)