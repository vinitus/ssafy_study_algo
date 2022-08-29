import sys
def input():
    return sys.stdin.readline().rstrip()

def findOne(arr):
    tmp = []
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 1:
                tmp.append((y,x))
    return tmp

def bfs(visited, one, dia, cnt, one_visited):
    global answer
    if one_visited[-1] == 1:
        if cnt > answer:
            answer = cnt
        return
    for i in range(len(one)):
        y,x = one[i][0], one[i][1]
        if not one_visited[i] and not visited["y"][y] and not visited["x"][x]:
            visited["y"][y] = 1
            visited["x"][x] = 1
            one_visited[i] = 1
            dia[y][x] = "B"
            bfs(visited,one,dia,cnt+1,one_visited)
            visited["y"][y] = 0
            visited["x"][x] = 0
            one_visited[i] = 0
            dia[y][x] = 1

N = int(input())
chess = list(list(map(int,input().split())) for _ in range(N))
dia1 = list(["*"] * (abs(i)) + [] for i in range(-N+1,N))
for j in range(N):
    for i in range(N):
        dia1[i+j] += [(chess[j][i]),"*"]
one = findOne(dia1)

visited = {"x":[0]*(2*N-1),"y":[0]*(2*N-1)}

one_visited = list([0] * len(one))
answer = 0
bfs(visited,one,dia1,0,one_visited)
print(answer)