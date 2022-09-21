import sys

def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

while True:
    n,k = map(int,input().split())
    if n == 0 and k == 0:
        break
    ancestor = dict()
    tree = dict()
    nums = list(map(int,input().split()))
    i = 1
    root = nums[0]
    tree[nums[0]] = []
    assign_to = [nums[0]]
    next_assign_to = []
    j = 0
    prev = -1
    while i < n:
        cur = nums[i]
        assign_numbers = [cur]
        next_assign_to.append(cur)
        i += 1
        prev = cur
        while i<n:
            cur = nums[i]
            if cur-prev ==1:
                assign_numbers.append(cur)
                next_assign_to.append(cur)
            else:
                break
            prev = cur
            i += 1
        tmp = assign_to.pop(0)
        tree[tmp] = assign_numbers
        for num in assign_numbers:
            ancestor[num] = tmp
        if not assign_to:
            assign_to = next_assign_to[:]
            next_assign_to = []
    ans = 0
    not_k = [root] + tree[root]
    if k in not_k:
        print(0)
        continue
    ignore = ancestor[k]
    rt = ancestor[ignore]
    tmp_list = tree[rt]
    for n in tmp_list:
        if n == ignore:
            continue
        if n in tree:
            ans += len(tree[n])
    print(ans)

