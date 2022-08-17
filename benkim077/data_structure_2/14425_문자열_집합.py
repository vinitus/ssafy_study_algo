N, M = map(int, input().split())
sett = set(input() for _ in range(N))
lst = list(input() for _ in range(M))

cnt = 0
for item in lst:
    if item in sett:
        cnt += 1

print(cnt)