import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    L = len(arr[1])
    dp = [[0] * L for _ in range(2)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]

    for i in range(2, L):
        dp[0][i] = max(dp[1][i-1], max(dp[0][i-2], dp[1][i-2])) + arr[0][i]
        dp[1][i] = max(dp[0][i-1], max(dp[0][i-2], dp[1][i-2])) + arr[1][i]

    print(max(dp[0][-1], dp[1][-1]))