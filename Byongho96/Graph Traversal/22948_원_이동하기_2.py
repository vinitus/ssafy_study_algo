# 1868 ms
from pprint import pprint
import sys
input = sys.stdin.readline

def dfs(v):
    visited = [0] * (N + 1)
    stk = []

    visited[v] = 1
    while True:
        # visit(v)
        if v == end:        # 끝지점을 만나면
            return stk          # 경로반환
        for w in adjLst[v]:
            if not visited[w]:
                stk.append(v)
                v = w
                visited[v] = 1
                break
        else:
            if stk:
                v = stk.pop()
            else:
                break

N = int(input())

# 시작점과 끝점 입력받기
# 데이터체커 백준 22942번
circles = [(-1010001, 0, 1)]
for _ in range(N):
    i, x, r = map(int, input().split())
    circles.append((x-r, i, 1))         # (위치, 원의 번호, 시작여부)
    circles.append((x+r, i, 0))
circles.append((1010001, 0, 0))
circles.sort()

start, end = map(int, input().split())

# 인접 리스트 만들기
adjLst = [[] for _ in range(N + 1)]
stk = [0]
for i in range(1, 2 * N + 2):
    open = circles[i][2]
    if open:
        adjLst[circles[i][1]].append(stk[-1])   # 스택의 마지막과 현재 원이 서로 인접
        adjLst[stk[-1]].append(circles[i][1])
        stk.append(circles[i][1])
    else:
        stk.pop()
# pprint(adjLst)

# dfs 탐색(반복구조로 경로 저장)
path = dfs(start) + [end]   # 마지막 도착지점 추가
print(len(path))
print(*path)