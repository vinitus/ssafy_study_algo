import sys
sys.stdin = open('input.txt')

N = int(input())
path = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = 0
i = 0
while i < N - 1:
    for j in range(i + 1, len(cost)):
        if cost[i] < cost[j]:
            pass
        else:
            for k in range(i, j):
                ans += cost[i] * path[k]
            break
    i += j - i

print(ans)