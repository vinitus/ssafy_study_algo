# 84ms
import sys
input = sys.stdin.readline

def dfs_recursive(n, cnt):
    # 종료조건
    if cnt == M:
        for i in range(N):
            if com_arr[i]:
                print(nums[i], end=' ')
        print()
        return
    elif n == N:
        return
    # 후보군 출력
    else:
        com_arr[n] = 1
        dfs_recursive(n + 1, cnt + 1)
        com_arr[n] = 0
        dfs_recursive(n + 1, cnt)
        return

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
nums.sort()

com_arr = [0] * N
dfs_recursive(0, 0)