# 332 ms
import sys
input = sys.stdin.readline

N = int(input())
adjLst = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 1:      # k가 단절점인가?
        if len(adjLst[k]) > 1:
            print('yes')
        else:
            print('no')
    else:           # k가 단절선인가
        print('yes')