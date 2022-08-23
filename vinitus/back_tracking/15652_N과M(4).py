import sys
def input():
    return sys.stdin.readline().rstrip()
N, M = map(int,input().split())
N_lst = list(i for i in range(1,N+1))
subset_lst = []

def subset():
    if len(subset_lst) == M:
        print(' '.join(map(str,subset_lst)))
        return
    
    for n in N_lst:
        if subset_lst and subset_lst[-1] > n:
            continue
        subset_lst.append(n)
        subset()
        subset_lst.pop()

subset()