import sys
sys.stdin = open('input.txt')


N = int(input())
data = []
for _ in range(N):
    p, n = map(int, input().split())
    data.append((p, n))
data.sort()

s = 0
e = N
ans = 1_000_000_000
while s <= e:
    center = (s + e) // 2
    sm_left = 0
    sm_right = 0

    for i in range(0, center + 1):
        sm_left += data[i][1]

    for i in range(center + 1, N):
        sm_right += data[i][1]

    if sm_left < sm_right:
        s = center + 1
    else:
        e = center - 1
        ans = min(ans, data[center][0])

print(ans)        

