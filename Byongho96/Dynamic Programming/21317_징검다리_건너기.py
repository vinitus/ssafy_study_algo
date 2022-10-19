# def dfs(step, energy, k):
#     global mn
#     if step == N:
#         mn = min(mn, energy)
#         return
#     if step > N:
#         return
#     if energy >= mn:
#         return
#     dfs(step + 1, energy + jump[step], k)
#     dfs(step + 2, energy + big_jump[step], k)
#     if k:
#         dfs(step + 3, energy + K, k-1)
#
#
# N = int(input())
# jump = [0] * N
# big_jump = [0] * N
# for i in range(1, N):
#     jump[i], big_jump[i] = map(int, input().split())
# K = int(input())
#
# mn = 5001 * (N -1)
# dfs(1, 0, 1)
# print(mn)

#########################################################################
# DP
# 하나를 더 만들어서, 하나가 다른 하나를 참조
N = int(input())
jump = [0] * N
big_jump = [0] * N
for i in range(1, N):
    jump[i], big_jump[i] = map(int, input().split())
K = int(input())

if N == 1:
    print(0)
elif N == 2:
    print(jump[1])
else:
    INF = 5001 * (N - 1)
    dp = [INF] * (N + 1)
    dp[1] = 0
    dp[2] = jump[1]
    dp[3] = min(dp[2] + jump[2], dp[1] + big_jump[1])

    big_dp = [INF] * (N + 1)

    for i in range(4, N + 1):
        dp[i] = min(dp[i-1] + jump[i-1], dp[i-2] + big_jump[i-2])
        big_dp[i] = min(big_dp[i-1] + jump[i-1], big_dp[i-2] + big_jump[i-2], dp[i-3] + K)  # 어차피 i-2에서 big jump를 안한 것들은, i-1에서 다 고려됨됨

    # print(dp)
    # print(big_dp)
    print(min(dp[-1], big_dp[-1]))