import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int,input().split()))
visited = [0] * N
to_move = int(input())
lst.sort()
cnt = N
q = []
flag = False

for i in range(N-1,-1,-1):
    if lst[i] < 0:
        pass
    else:
        if not visited[lst[i]]:
            visited[lst[i]] = 1
            cnt -= 1

print(cnt)