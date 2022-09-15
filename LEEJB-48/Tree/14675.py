import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

N = int(input())
tree = [[]for _ in range(N+1)]

for _ in range(N-1):
    n1,n2 = map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)


q = int(input())

for _ in range(q):
    t,k = map(int,input().split())
    if t ==2:
        print("yes")
    else:
        if len(tree[k]) == 1:
            print("no")
        else:
            print("yes")