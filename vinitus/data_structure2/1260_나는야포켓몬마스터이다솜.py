import sys
input = sys.stdin.readline

N, M = map(int,input().split())

dct = {}
dct1 = {}
for i in range(1, N+1):
    tmp = input().strip()
    dct[f"{i}"] = tmp
    dct1[tmp] = f"{i}"

for _ in range(M):
    i = input().strip()
    if i.isdigit():
        print(dct[i])
    else:
        print(int(dct1[i]))