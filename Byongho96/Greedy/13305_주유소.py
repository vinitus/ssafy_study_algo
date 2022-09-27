# 160ms
import sys
input = sys.stdin.readline

N = int(input())
road = [0] + list(map(int, input().split()))
oil = list(map(int, input().split()))
oil[-1] = 0                 # 마지막 주유소는 가장 최소 0원

mn = oil[0]                 # 초기 최솟값은 첫번째 주유소
price = 0
distance = 0
for i in range(1, N):       # 진행하면서 최솟값의 주유소를 만날때마다 가격 업데이트
    distance += road[i]
    if oil[i] < mn:
        price += distance * mn
        mn = oil[i]
        distance = 0

print(price)
