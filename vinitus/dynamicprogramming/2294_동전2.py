import sys
def input():
    return sys.stdin.readline().rstrip()

def sol(N,K):
    dp = [0] + [10001] * (K)
    for _ in range(N):
        num = int(input())
        if num == K:
            print(1)
            return
            
        for i in range(num,K+1):
            dp[i] = min(dp[i], dp[i-num]+1)
            
    if dp[-1] == 10001:
        print(-1) 
        return
    else:
        print(dp[-1])
        return
sol(*map(int,input().split()))
