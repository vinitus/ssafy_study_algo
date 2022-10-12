import sys
input = sys.stdin.readline

def factorial(n):
    if n <= 1:
        return 1
    if memo[n]:
        return memo[n]
    memo[n] = n * factorial(n-1)
    return memo[n]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # N + 1 개 중에서 중복을 허용하여 M - N개를 뽑는 경우의 수
    # N + 1 H M - N
    # M C M - N
    memo = [0] * 31
    print(factorial(M) // factorial(M - N) // factorial(N))

    # M 개 중에서 N개를 뽑는 경우의 수
    # M C N
