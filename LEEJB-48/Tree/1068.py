import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

N = int(input())
tree_info = list(map(int,input().split()))
delete_node = int(input())
tree = [[] for _ in range(N+1)]

for i,v in enumerate(tree_info): #i는 해당 노드, v는 부모
    if v == -1:
        root = i
    else:
        tree[v].append(i)
if root == delete_node:
    print(0)
else:
    tree[tree_info[delete_node]].remove(delete_node)
    def traverse(rt):
        stack = [rt]
        ret = 0

        while stack:

            cur = stack.pop()
            if not tree[cur]:
                ret +=1

                continue
            for num in tree[cur]:
                stack.append(num)
        return ret

    print(traverse(root))