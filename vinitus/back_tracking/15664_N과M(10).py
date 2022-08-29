import sys
def input():
    return sys.stdin.readline().rstrip()

def subset(subset_arr, visited):
    if len(subset_arr) == M:
        print(" ".join(map(str,subset_arr)))
        return
    tmp = 0
    for idx in range(N):
        if not visited[idx] and tmp != N_lst[idx]:
            if subset_arr and subset_arr[-1] > N_lst[idx]:
                continue
            subset_arr.append(N_lst[idx])
            visited[idx] = [1]
            tmp = N_lst[idx]
            subset(subset_arr, visited)
            visited[idx] = 0
            subset_arr.pop()

N, M = map(int,input().split())
N_lst = list(map(int,input().split()))
N_lst.sort()
subset_lst = []
visited = [0] * N

subset(subset_lst, visited)