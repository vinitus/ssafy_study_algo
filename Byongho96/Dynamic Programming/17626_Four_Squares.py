# DP 밑에서부터 차례대로, 반드시 dp[n-1] + dp[n-2] 등의 구조가 아님!!
N = int(input())
dp = [0] * (N + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, N + 1):
    mn = N + 1
    for j in range(1, int(i**0.5) + 1):
        mn = min(mn, dp[i - j**2])
    dp[i] = mn + 1

print(dp[N])

# memo
N = int(input())
memo = [0] * (N + 1)

def squares(n):
    print(n)
    if n <= 1:
        return n
    if memo[n]:
        return memo[n]
    mn = N + 1
    for i in range(1, int(n**0.5) + 1):
        mn = min(mn, squares(n - i**2))
    memo[n] = mn + 1
    return memo[n]

print(squares(N))
print(memo)

# def squares(n):
#     print(n)
#     if n <= 1:
#         return n
#     if memo[n]:
#         return memo[n]
#     memo[n] = 1 + squares(n - int(n**0.5)**2)
#     return memo[n]
#
# memo = [0]* 50001
# n = int(input())
#
# print(squares(n))