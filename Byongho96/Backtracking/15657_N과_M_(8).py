# 92ms

import sys
input = sys.stdin.readline

def dfs_recursive(cnt, si):
    if cnt == M:
        print(*selected)
        return
    else:
        for i in range(si, N):
            selected[cnt] = nums[i] # 초기화해줄 필요 없음. 어차피 모두 overwritten
            si = i
            dfs_recursive(cnt + 1, si)
        return

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

selected = [0] * M
dfs_recursive(0, 0)