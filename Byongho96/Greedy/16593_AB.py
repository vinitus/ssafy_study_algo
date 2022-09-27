# 68ms
# B에서 A를 만드는 방향
A, B = map(int, input().split())

result = 1
while B > A:
    if not B % 2:
        B //= 2
        result += 1
    elif B % 10 == 1:
        B //= 10
        result += 1
    else:
        result = -1
        break

if B != A:
    result = -1

print(result)
