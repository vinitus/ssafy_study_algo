import sys
def input():
    return sys.stdin.readline().rstrip()

def check(y,x,N):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

def findOne(arr,N):
    tmp = []
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                tmp.append((y,x))
    return tmp

def cntOne(y,x,arr):
    global N, cnt_queen
    d = [(1,1),(-1,-1),(-1,1),(1,-1)]
    for idx in range(4):
        dy, dx = d[idx][0], d[idx][1]
        my,mx = y+dy,x+dx
        while check(my,mx,N):
            if arr[my][mx] == 1:
                cnt_queen[y][x][idx//2] += 1
            my += dy
            mx += dx

def queen1(arr,N,one):
    global answer, cnt_queen
    for y, x in one:
        cntOne(y,x,arr)
        cnt_queen[y][x][0] += 1
        cnt_queen[y][x][1] += 1
        if cnt_queen[y][x][0] + cnt_queen[y][x][1] == 2:
            cnt_queen[y][x] = "B"
            answer += 1

N = int(input())
chess = list(list(map(int,input().split())) for _ in range(N))
one = findOne(chess,N)
cnt_queen = list(list([0,0] for _ in range(N)) for _ in range(N))
answer = 0
queen1(chess,N,one)
for i in cnt_queen:
    print(*i)