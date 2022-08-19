# 756ms
import sys
input = sys.stdin.readline

N = int(input())
towers = list(enumerate(map(int, input().rstrip().split())))
stk = []
ans = [0] * N

for t in towers[::-1]:
    while stk and t[1] >= stk[-1][1]:
        s = stk.pop()
        ans[s[0]] = t[0] + 1
    else:
        stk.append(t)

print(*ans)