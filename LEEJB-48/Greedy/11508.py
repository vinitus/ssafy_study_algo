import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort(reverse=True)
ans = sum(nums)
if N <= 2:
    print(ans)
else:
    for i in range(2,N,3):
        ans -= nums[i]
print(ans)