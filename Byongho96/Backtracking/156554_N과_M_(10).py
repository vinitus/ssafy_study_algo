# 68ms
import sys
input = sys.stdin.readline

def dfs_recursive(n, cnt):
    # 종료조건
    if cnt == M:
        tmp = []
        for i in range(n):
            if arr[i]:
                tmp.append(nums[i])
        if tmp not in rlt:
            rlt.append(tmp)
        return
    elif n == N:
        return
    # 후보군 출력
    else:
        arr[n] = 1
        dfs_recursive(n + 1, cnt + 1)
        arr[n] = 0
        dfs_recursive(n + 1, cnt)
        return

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
nums.sort()

rlt = []
arr = [0] * N
dfs_recursive(0, 0)

# rlt = sorted(list(set(rlt))) set은 안의 요소가 hashable한 불변의 객체여야 한다
for ele in rlt:
    print(*ele)