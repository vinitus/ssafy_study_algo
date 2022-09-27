import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")


#############################


def backtracking(n, cnt):
    if n == 0:
        return cnt
    for i in range(n):
        if M[i] + i >= n:
            return backtracking(i, cnt + 1)


T = int(input())

for test_case in range(1, T + 1):
    N, *M = list(map(int, input().split()))

    ans = backtracking(N - 1, 0)

    print(f"#{test_case} {ans - 1}")
