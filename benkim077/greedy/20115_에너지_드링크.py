import sys
sys.stdin = open('input.txt')


N = int(input())
data = list(map(int, input().split()))
data.sort()

ans = data[-1]
for i in range(N - 1):
    ans += data[i] / 2

print(ans)