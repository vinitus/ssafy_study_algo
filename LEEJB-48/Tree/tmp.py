import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

T = 10

for test_case in range(1,T+1):
    N = int(input())
    tree = [None] * (N+1)
    tree_structure = [None] * (N+1)
    for i in range(N):
        p = input().split()
        if len(p) == 2:
            node,num = map(int,p)
            tree[node] = num
        else:
            node,oper,child1,child2 = p
            node = int(node)
            child1,child2 = int(child1),int(child2)
            tree[node] = oper
            tree_structure[node] = [child1,child2]
    def calculate(n):
        if str(tree[n]).isdigit():
            return tree[n]
        elif tree[n] == '+':
            return calculate(tree_structure[n][0]) +calculate(tree_structure[n][1])
        elif tree[n] == '-':
            return calculate(tree_structure[n][0]) -calculate(tree_structure[n][1])
        elif tree[n] == '/':
            return calculate(tree_structure[n][0]) /calculate(tree_structure[n][1])
        elif tree[n] == '*':
            return calculate(tree_structure[n][0]) *calculate(tree_structure[n][1])
    print(f"#{test_case} {int(calculate(1))}")