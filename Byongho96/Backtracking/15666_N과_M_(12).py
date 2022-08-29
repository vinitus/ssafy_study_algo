# 320ms
# combinations_with_replacement
import sys
input = sys.stdin.readline

def dfs_recursive(cnt, pre_idx):
    # 종료조건
    if cnt == M:
        tmp = []
        for arr_i in range(M):
            tmp.append(nums[arr[arr_i]])
        if tmp not in rlt:
            rlt.append(tmp)
        return
    # 후보군 출력
    else:
        for i in range(pre_idx, N):
            arr[cnt] = i
            dfs_recursive(cnt + 1, i)
        return

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
nums.sort()

rlt = []
arr = [0] * M
dfs_recursive(0, 0)

for ele in rlt:
    print(*ele)
