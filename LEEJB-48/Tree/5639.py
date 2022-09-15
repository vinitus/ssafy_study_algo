import sys
sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################
tree = list(map(int,input().split()))
while True:
    try:
        tree.append(int(input()))
    except:
        break
def preorder_to_postorder(tr):
    rt = tr[0]
    index = len(tr)
    for i,v in enumerate(tr):
        if v > rt:
            index = i
            break
    left = tr[1:index]
    right = tr[index:]
    if left:
        preorder_to_postorder(left)
    if right:
        preorder_to_postorder(right)
    print(rt)
preorder_to_postorder(tree)