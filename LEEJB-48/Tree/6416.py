import sys


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################
case = 1
all_out = False
while True:
    fr = set()
    to = set()
    not_tree = False
    tmp_parent_to_child = []
    while True:
        #################
        nums = input().split("  ")
        if len(nums) == 1:
            if not nums[0]:
                continue
            """a, b = map(int, nums[0].split())
            if a < 0 and b < 0:
                all_out = True
                break
            if a == 0 and b == 0:
                break"""
        exit_condition = nums[-1]
        a,b = map(int,exit_condition.split())
        if a==0 and b ==0:
            nums.pop()
            tmp_parent_to_child += nums
            break
        if a<0 and b <0:
            all_out = True
            break
        tmp_parent_to_child += nums

    if all_out:
        break
    if not tmp_parent_to_child:
        print(f"Case {case} is a tree.")
        case += 1
        continue
    if not not_tree:
        for pair in tmp_parent_to_child:
            parent,child = map(int,pair.split())
            fr.add(parent)
            if child in to:
                not_tree = True
                break
            to.add(child)
        if len(fr-to) != 1:
            not_tree = True
    if not_tree:
        print(f"Case {case} is not a tree.")
    else:
        print(f"Case {case} is a tree.")
    case += 1