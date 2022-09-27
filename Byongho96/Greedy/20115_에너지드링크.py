import sys
input = sys.stdin.readline

N = int(input())
drinks = list(map(int, input().split()))

drinks.sort()

result = drinks[-1] + sum(drinks[:-1]) / 2

print(result)