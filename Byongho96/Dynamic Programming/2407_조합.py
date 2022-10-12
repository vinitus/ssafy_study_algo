def factorial(n):
    if n <= 1:
        return 1
    if memo[n]:
        return memo[n]
    memo[n] = n * factorial(n-1)
    return memo[n]

N, M = map(int, input().split())
memo = [0] * 101
# N C M
print(factorial(N) // factorial(N-M) // factorial(M))
