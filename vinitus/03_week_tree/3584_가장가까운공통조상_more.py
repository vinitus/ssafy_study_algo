import sys

input = sys.stdin.readline

def find_parent(a, b):
    # 조상 리스트 만들기
    a_parent = [a]
    while tree[a]:
        a = tree[a]
        a_parent.append(a)

    # 조상 중 하나가 b다
    if b in a_parent:
        return b

    # b의 조상을 찾아서 올라감. a랑 겹치면 바로 return
    while tree[b]:
        b = tree[b]
        if b in a_parent:
            return b
# 저는 B를 만들었는데 이 분은 B를 만들지 않았음.
# 저는 A, B 둘 다 트리를 타고 끝까지 올라갔는데 이 분은 만들어둔 A 트리를 B를 통해서 타고 올라감
# if 구문을 통한 최적화도 되어있음
# 저는 1500ms 나왔고 이분은 92ms


T = int(input())
for _ in range(T):
    N = int(input())
    tree = [0] * (N+1)
    for __ in range(N-1):
        p, c = map(int, input().split())
        tree[c] = p
    a, b = map(int, input().split())
    print(find_parent(a, b))
