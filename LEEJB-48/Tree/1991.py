import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

N = int(input())
left_dict = {}
right_dict = {}
for _ in range(N):
    node,left,right = input().split()
    if left != '.':
        left_dict[node] = left
    if right != '.':
        right_dict[node] = right
ans_pre = []
ans_in = []
ans_post = []
def preorder(rt):
    ans_pre.append(rt)
    if rt in left_dict:
        preorder(left_dict[rt])
    if rt in right_dict:
        preorder(right_dict[rt])
def inorder(rt):
    if rt in left_dict:
        inorder(left_dict[rt])
    ans_in.append(rt)
    if rt in right_dict:
        inorder(right_dict[rt])
def postorder(rt):
    if rt in left_dict:
        postorder(left_dict[rt])
    if rt in right_dict:
        postorder(right_dict[rt])
    ans_post.append(rt)
preorder('A')
inorder('A')
postorder('A')
print(''.join(ans_pre))
print(''.join(ans_in))
print(''.join(ans_post))
