# 132ms
import sys
input = sys.stdin.readline

N = int(input())
price = [0] * N
for i in range(N):
    price[i] = int(input())
price.sort(reverse=True)

a, b = divmod(N, 3)
result = 0
# 2 + 1 상품 계산
for i in range(a):
    result += price[3 * i]
    result += price[3 * i + 1]

# 정가 계산
for i in range(b):
    result += price[3 * a + i]

print(result)
