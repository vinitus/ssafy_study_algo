import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
data = [int(input()) for _ in range(N)]

cnt = 0
for i in range(N - 1, -1, -1):
    if K // data[i] > 0:
        cnt += K // data[i]
        K = K % data[i]
    if K == 0:
        break

print(cnt)
    

