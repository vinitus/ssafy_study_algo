N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    mn = dp[i - 1]
    if not i % 2:
        mn = min(mn, dp[i // 2])
    if not i % 3:
        mn = min(mn, dp[i // 3])
    dp[i] = mn + 1

# print(dp)
print(dp[N])