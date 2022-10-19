import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())

lst = [[0 for _ in range(N+1)]]
for i in range(N):
    tmp = [0] + list(map(int,input().split()))
    tmp[1] += lst[i][1]
    for j in range(2,N+1):
        tmp[j] += lst[i][j] - lst[i][j-1] + tmp[j-1]
    lst.append(tmp)

for _ in range(M):
    y1,x1,y2,x2 = map(int,input().split())
    answer = lst[y2][x2] - lst[y1-1][x2] - lst[y2][x1-1] + lst[y1-1][x1-1]
    print(answer)