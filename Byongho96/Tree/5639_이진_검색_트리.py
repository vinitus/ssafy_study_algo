# 4036 ms
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


##############################################
nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

def pre_to_post(nums):
    if len(nums) == 0:
        return
    elif len(nums) == 1:
        print(nums[0])
        return
    root = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > root:
            # 왼쪽노드
            pre_to_post(nums[1:i])
            # 오른족노드
            pre_to_post(nums[i:])
            print(root)
            return
    else:
        pre_to_post(nums[1:])
        print(root)

pre_to_post(nums)


#####################################
# 이런식으로 조건문을 최소화할 수 있음!!
import sys
sys.setrecursionlimit(10**9)
def f(start, end):
    if start > end:
        return
    else:
        root = pre[start]
        div = end + 1
        for pos in range(start+1, end+1):
            if root < pre[pos]:
                div = pos
                break
        f(start+1, div-1)
        f(div, end)
        print(root)

pre = []
while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break
if pre:
    f(0, len(pre)-1)
