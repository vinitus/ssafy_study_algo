from heapq import heappop,heappush
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = []
for _ in range(N):
    tmp = list(map(int,input().split()))
    idx = 0
    tmp.sort(reverse=True)
    while lst and idx < N:
        a = heappop(lst)
        if tmp[idx] > a:
            heappush(lst, tmp[idx])
            idx += 1
        else:
            heappush(lst, a)
            break
    else:
        for i in tmp:
            heappush(lst, i)

print(heappop(lst))