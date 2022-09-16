import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################
N,W = map(int,input().split())
tree = [0]*(N+1)
for _ in range(N-1):
    U,V = map(int,input().split())
    tree[U] += 1
    tree[V] += 1
cnt = 0
for i in range(2,len(tree)):
    if tree[i] == 1:
        cnt += 1
print(W/cnt)