import sys
input = sys.stdin.readline

# 26개의 리스트로 만들어도 되고, 844ms
# 딕셔너리 형태로 만들어도 됨

# abc -> abc, acb, bac, bca, cab, cba
# aabc -> abac, abac

# [ 1, 1, 0, 4, 0, .... 0 ] 26
#   a  b  c  d  e  .... z
def dfs_recursive(n):
    if n == N:
        print(''.join(ans))
        return
    else:
        for i in range(26):
            if alpha[i]:
                alpha[i] -= 1
                ans[n] = chr(i + ord('a'))
                dfs_recursive(n + 1)
                alpha[i] += 1

T = int(input())

for _ in range(T):
    string = sorted(input().rstrip())
    N = len(string)

    alpha = [0] * 26
    ans = [0] * N
    for s in string:
        alpha[ord(s) - ord('a')] +=1

    dfs_recursive(0)

## 단어를 만들고, 그게 이전에 만들었는지 확인하고 하는것은 시간초과
# def dfs_recursive(n):
#     # 종료조건
#     if n == N:
#         tmp = ''.join(arr)
#         if tmp not in ans:
#             print(tmp)
#             ans.add(tmp)
#         return
#     else:
#         for i in range(N):
#             if not selected[i]:
#                 selected[i] = 1
#                 arr[n] = string[i]
#                 dfs_recursive(n+1)
#                 selected[i] = 0
#         return
#
# T = int(input())
#
# for _ in range(T):
#     string = sorted(input().rstrip())
#     N = len(string)
#
#     arr = [0] * N
#     selected = [0] * N
#     ans = set()
#     dfs_recursive(0)