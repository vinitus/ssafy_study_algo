import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [0] * N
for i in range(N):
    coins[i] = int(input())

# Greedy
num = 0
for coin in coins[::-1]:
    a, b = divmod(K, coin)
    num += a
    K = b
    if K == 0:
        break

print(num)

# # DP 메모리초과
# DP = [K + 1] * (K + 1)
# DP[0] = 0
# for i in range(1, K + 1):
#     for coin in coins:
#         if i - coin < 0:
#             break
#         else:
#             DP[i] = min(DP[i-coin] + 1, DP[i])
#
# print(DP[-1] if DP[-1] != K + 1 else -1)
