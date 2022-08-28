import sys


def input():
    return sys.stdin.readline().rstrip()


def backtracking(i, num):
    if i == 10:
        if num:
            nums.append(int(num))
        return None
    backtracking(i + 1, num + target_num[i])
    backtracking(i + 1, num)


N = int(input())
target_num = '9876543210'
nums = []
backtracking(0, '')
nums.sort()
if N <= len(nums):
    print(nums[N - 1])
else:
    print(-1)
