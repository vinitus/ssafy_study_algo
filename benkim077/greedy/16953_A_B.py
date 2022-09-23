# A, B
# B가 2로 나누어 떨어지지 않으면, 1을 없앤다.
import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())

cnt = 0
while A < B:
    if B % 2:
        if B % 10 == 1:
            B //= 10
        else:
            print(-1)
            exit()
    
    else:
        B //= 2
    cnt += 1


if A == B:
    print(cnt + 1)
else:
    print(-1)