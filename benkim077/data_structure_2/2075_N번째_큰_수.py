'''
- 메모리 초과로 pypy로 제출

- mx 값 설정 잘하기

- heapq를 굳이 사용하진 않았음
'''


import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for _ in range(N):
    mx = -1000000001
    idx = -1
    for i in range(N):
        if mx < arr[i][len(arr[i]) - 1]:
            mx = arr[i][len(arr[i]) - 1]
            idx = i
    ans = arr[idx].pop()

print(ans)
