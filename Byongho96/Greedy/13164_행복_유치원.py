# 296 ms
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# K - 1 개의 큰 수를 제외한 나머지 수의 합
nums = list(map(int, input().split()))

diff = [0] * (N - 1)
for i in range(N - 1):
    diff[i] = nums[i + 1] - nums[i]

diff.sort(reverse=True)
result = sum(diff[K-1:])
print(result)