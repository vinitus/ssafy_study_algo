import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
N_lst = list(map(int,input().split()))
N_lst.sort()
subset_lst = []
answer = []

# def subset():
#     if len(subset_lst) == M:
#         print(" ".join(map(str,subset_lst)))
#         return
    
def subset():
    if len(subset_lst) == M:
        if subset_lst not in answer:
            answer.append(subset_lst)
            print(" ".join(map(str,subset_lst)))
        return
    
    for idx in N_lst:
        if idx not in subset_lst:
            print(subset_lst)
            subset()
            subset_lst.pop()

subset()
