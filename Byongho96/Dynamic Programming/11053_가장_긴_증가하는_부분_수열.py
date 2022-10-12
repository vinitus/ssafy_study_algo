N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N    # dp[i] : nums[i]를 마지막 숫자로 하는 부분 수열 중 가장 긴 것
for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))