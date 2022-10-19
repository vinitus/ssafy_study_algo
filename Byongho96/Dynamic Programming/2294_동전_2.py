from collections import deque
import sys
input = sys.stdin.readline

'''
https://www.acmicpc.net/problem/2294
입력예제
3 15
1
5
12
'''
##########################################################################################################################################################
# [1]번 해법. DP로 풀기
# 풀이 코드 자체는 17626번 Four Squares와 유사

INF = 10001                        # 최대 동전 사용 갯수 + 1: 나올 수 없는 값
N, K = map(int, input().split())
coins = [0] * N
for i in range(N):                  # 동전 종류 리스트: coins = [1, 5, 12]
    coins[i] = int(input())

dp = [INF] * (K + 1)                # DP리스트는 모두 최댓값으로 설정. DP[k]를 읽었을 때 INF가 나오면 불가능한 값임을 알 수 있음. 또함 만약 불가능한 값을 -1로 설정하면 28번째 줄에서 min함수 사용 시 원하는대로 동작을 하지 않음
dp[0] = 0                           # DP[0] = 0으로 설정
                                    # 이렇게 해야지 밑에 for문을 돌면서, dp[1] = 1, dp[5] = 1, dp[12] = 1이 되면서, 의도한 바대로 dp값이 채워짐

# 코드[1]과 코드[2]는 동일한 내용의 코드
# 코드[2]가 코드[1]보다 더 보편적이고, 조금 더 효율적임
############################## 코드 [1] ######################################
# 620 ms
for i in range(1, K + 1):           # DP를 1번부터 K번까지 채워줄 것임
    for j in range(N):                  # dp[i] = dp[i-coin]의 값 중 가장 작은 것 + 1  // coin은 coins 리스트에 있는 동전 종류
        if i - coins[j] >= 0:               # 초반단계에서(i < max(coins) 일 때), i-coin 값이 음수가 나온다면, 해당 조합으로는 i값은 만들 수 없으므로 고려 X
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)
#############################################################################

# ############################## 코드 [2] ######################################
# # 432 ms
# for coin in coins:                  # 모든 동전 타입에 대해 반복
#     for i in range(coin, K + 1):        # 애초에 coin의 값부터 K까지 채워 넣음으로써, i-coin이 0미만이 되는 일이 없도록 함
#         dp[i] = min(dp[i], dp[i-coin] + 1)
# #############################################################################

# print(dp)
result = dp[K]
if result == INF:                   # 값을 읽었을 때, INF가 나오면 해당 K원은 형성 불가능
    print(-1)
else:
    print(result)

##########################################################################################################################################################

# [2]번 해법. BFS로 풀기. 200ms

def bfs(coins):
    visited = set(coins)

    q = deque()
    for coin in coins:
        q.append((1, coin))

    while q:
        cnt, sm = q.popleft()
        if sm == K:
            print(cnt)
            return
        for add_coin in coins:
            new_sm = sm + add_coin
            if new_sm <= K and new_sm not in visited:
                visited.add(new_sm)
                q.append((cnt+1, new_sm))

    print(-1)
    return

N, K = map(int, input().split())
coins = set()
for i in range(N):
    coin = int(input())
    if coin <= K:
        coins.add(coin)

bfs(coins)

##########################################################################################################################################################
# [3]번 도전. memoization 활용한 재귀로 풀기. Recursion Error 발생
# INF = 10001
#
# def mn_coin(k):
#     if k < 0:
#         return INF
#     if k == 0:
#         return 0
#     if memo[k]:
#         return memo[k]
#     mn = INF
#     for i in range(N):
#         mn = min(mn, mn_coin(k - coins[i]))
#     memo[k] = mn + 1
#     return memo[k]
#
# N, K = map(int, input().split())
# coins = [0] * N
# for i in range(N):
#     coins[i] = int(input())
#
# memo = [0] * (K + 1)
# print(mn_coin(K))