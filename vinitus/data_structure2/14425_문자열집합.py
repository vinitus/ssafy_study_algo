import sys
input = sys.stdin.readline

S = set()
N,M = map(int,input().split())
for _ in range(N):
    S.add(input())
S_answer = set()
cnt = 0
for _ in range(M):
    tmp = input()
    if tmp in S:
        cnt += 1
print(cnt)