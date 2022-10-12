import sys
input = sys.stdin.readline

# 후......................................
N = int(input())
stairs = [0] * (N + 1)
for i in range(1, N + 1):
    stairs[i] = int(input())

if N == 1:
    print(stairs[1])

elif N == 2:
    print(stairs[1] + stairs[2])

else:
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])
    print(dp[N])

# def backtracking(n, sm, consecutive):
#     global mx
#     if n == N:
#         mx = max(mx, sm + stairs[n])
#         return
#     if n > N:
#         return
#     if consecutive == 1:
#         backtracking(n + 2, sm + stairs[n], 0)
#     else:
#         backtracking(n + 1, sm + stairs[n], consecutive + 1)
#         backtracking(n + 2, sm + stairs[n], 0)
#
#
# N = int(input())
# stairs = [0] * (N + 1)
# for i in range(1, N + 1):
#     stairs[i] = int(input())
#
#     mx = 0
#     backtracking(0, 0, -1)
#
#     print(mx)
