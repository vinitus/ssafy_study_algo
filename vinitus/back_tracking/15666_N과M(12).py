import sys
def input():
    return sys.stdin.readline().rstrip()

def subset(subset_arr, visited):
    if len(subset_arr) == M:
        print(" ".join(map(str,subset_arr)))
        return
    for idx in range(N):
        if subset_arr and subset_arr[-1] > N_lst[idx]:
            continue
        subset_arr.append(N_lst[idx])
        visited[idx] = [1]
        subset(subset_arr, visited)
        visited[idx] = 0
        subset_arr.pop()

N, M = map(int,input().split())
N_lst = list(map(int,input().split()))
N_lst = list(set(N_lst))
N_lst.sort()
N = len(N_lst)
subset_lst = []
visited = [0] * N

subset(subset_lst, visited)