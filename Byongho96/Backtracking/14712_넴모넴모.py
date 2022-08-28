# PyPy 3872ms
import sys
input = sys.stdin.readline

def isPromising(i, j):
    if arr[i][j-1] and arr[i-1][j-1] and arr[i-1][j]:
        return False
    return True

def dfs_recursive(i, j):
    global cnt
    if i == N and j == M + 1:
        cnt += 1
        return
    else:
        if j == M + 1:
            i += 1
            j = 1
        if isPromising(i, j):
            arr[i][j] = 1
            dfs_recursive(i, j+1)
        arr[i][j] = 0
        dfs_recursive(i, j+1)
        return


N, M = map(int, input().rstrip().split())
arr = [[0] * (M + 2) for _ in range(N)]
arr = [[0] * (M + 2)] + arr + [[0] * (M + 2)]

cnt = 0
dfs_recursive(1, 1)

print(cnt)