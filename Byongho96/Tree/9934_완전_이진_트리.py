# 중위 순회로 입력값 트리 만들기
def inorder(cur):
    global last
    if cur <= 2**K - 1:
        inorder(2 * cur)
        tree[cur] = nums[last]
        last += 1
        inorder(2 * cur + 1)

K = int(input())
nums = list(map(int, input().split()))

tree = [0] * (2**K)
last = 0
inorder(1)

for i in range(K):
    print(*tree[2**i:2**(i+1)])
