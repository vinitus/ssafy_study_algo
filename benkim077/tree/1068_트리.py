'''
노드의 개수 N(50보다 작거나 같은 자연수)
루트는 -1
리프 노드의 갯수를 구하라
'''
import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, value, child, parent):
        self.value = value
        self.child = child
        self.parent = parent


def del_node(node_num):
    if tree[node_num].child == []:
        del tree[node_num]
        return 

    for child_node in tree[node_num].child:
        del_node(child_node)
    del tree[node_num]
    return

# 입력 처리
N = int(input())                            #  5
data = list(map(int, input().split()))      # -1 0 0 1 1
deleted_node = int(input())                     #  2

# 트리, 노드를 생성
tree = {}
# for i in range(N):  
#     tree[i] = Node(i, [], None)

# 노드와 부모 노드를 연결
tree[0] = Node(0, [], None)
k = 1
for p_node_v in range(0, N):
    for i in range(len(data)):
        if data[i] == p_node_v:
            tree[k] = Node(k, [], data[i])
            tree[data[i]].child.append(k)
            k += 1

for node in tree:
    print(tree[node].value, tree[node].child, tree[node].parent)            
                

            




# for i in range(len(data)):  
#     if data[i] == -1:
#         pass
#     else:
#         tree[i].parent = data[i]
#         tree[data[i]].child.append(i)


# deleted_node 처리
if deleted_node != 0:
    tree[tree[deleted_node].parent].child.pop(tree[tree[deleted_node].parent].child.index(deleted_node))    # 자식 노드 연결 제거
# tree[deleted_node].parent = None    # 부모 노드 연결 제거
del_node(deleted_node)


for node in tree:
    print(tree[node].value, tree[node].child, tree[node].parent)


ans = 0
if tree:
    for node in tree:
        if tree[node].child == []:
            ans += 1

print(ans)

