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
        if one_visited[i]:
            continue
        y,x = one[i][0], one[i][1]
        if not visited["y"][y] and not visited["x"][x]:
            visited["y"][y] = 1
            visited["x"][x] = 1
            one_visited[i] = 1
            bfs(visited,one,dia,cnt+1,one_visited)
            visited["y"][y] = 0
            visited["x"][x] = 0

N = int(input())
dia1 = list(["*"] * (abs(i)) + [] for i in range(-N+1,N))
one = []
for j in range(N):
    tmp = list(map(int,input().split()))
    for i in range(N):
        if tmp[i] == 1:
            one.append((i+j,abs(-N+1+j+i)+2*(i+j)))
        dia1[i+j] += [tmp[i],"*"]

# [(0, 4), (1, 3), (2, 4), (2, 6), (3, 1), (3, 7), (4, 0), (4, 4), (4, 8), (6, 2), (6, 6), (7, 5), (8, 4)]
one.sort()
for i in dia1:
    print(*i)
print(one)
visited = {"x":[0]*(2*N-1),"y":[0]*(2*N-1)}

one_visited = list([0] * len(one))
answer = 0
bfs(visited,one,dia1,0,one_visited)
print(answer)