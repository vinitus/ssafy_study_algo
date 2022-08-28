# 76ms
import sys
input = sys.stdin.readline

def dfs_recursive():
    ans.append(int(''.join(map(str, num_arr)))) # append할때 숫자와해서 append
    for i in range(num_arr[-1]):
        num_arr.append(i)
        dfs_recursive()
        num_arr.pop()


N = int(input())

ans = []
for i in range(10):
    num_arr = [i]
    dfs_recursive()

ans.sort()
ans_len = len(ans)
if N > ans_len:
    print(-1)
else:
    print(ans[N-1])