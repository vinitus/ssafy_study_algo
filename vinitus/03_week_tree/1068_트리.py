import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int,input().split()))
visited = [0] * N
to_move = int(input())
visited[to_move] = 1
lst[to_move] = -1
cnt = N - 1
q = [to_move]

while q:
    tmp = q.pop()
    for i in range(N):
        if lst[i] == tmp:
            q.append(i)
            if not visited[i]:
                visited[i] = 1
                lst[i] = -1
                cnt -= 1

for i in range(N-1,-1,-1):
    if lst[i] < 0:
        pass
    else:
        if not visited[lst[i]]:
            visited[lst[i]] = 1
            cnt -= 1

print(cnt)