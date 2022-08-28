import sys


def input():
    return sys.stdin.readline().rstrip()


def backtracking(i, arr):
    global ans
    if i == length:
        return None
    share, remainder = divmod(i, M)
    if share >= 1 and remainder >= 1:
        # 대충 있는지 체크
        if arr[i - 1] and arr[i - M] and arr[i - M - 1]:
            ans -= 2 ** (length - i - 1)
            backtracking(i + 1, arr[:])
        else:
            backtracking(i + 1, arr[:])
            arr[i] = True
            backtracking(i + 1, arr[:])
    else:
        backtracking(i + 1, arr[:])
        arr[i] = True
        backtracking(i + 1, arr[:])


N, M = map(int, input().split())
length = N * M
ans = 2 ** length
arr = [False] * length
if N == 1 or M == 1:
    print(ans)
else:
    backtracking(0, arr)
    print(ans)
