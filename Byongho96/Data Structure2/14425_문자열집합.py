# 140ms
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

s = set()
for _ in range(N):
    s.add(input().rstrip())

cnt = 0
for _ in range(M):
    if input().rstrip() in s:
        cnt += 1
print(cnt)