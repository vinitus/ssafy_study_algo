# 176 ms
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

mx = 0
total_sum = sum(nums[1:-1])
cumulative_sum = 0          # 누적합으로 sum함수 사용을 최소화
for i in range(1, N-1):
    # 벌통이 왼쪽
    left = total_sum - nums[i] + cumulative_sum + 2 * nums[0]
    cumulative_sum += nums[i]
    # 벌통이 오른쪽
    right = 2 * total_sum - nums[i] - cumulative_sum + 2 * nums[-1]

    mx = max(mx, left, right)

# 벌통이 중앙
mx = max(mx, total_sum + max(nums[1:-1]))

print(mx)