# 내가 푼 것
import sys
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int,input().split())
lst = list(map(int,input().split()))

def cal(s,e,s_h,e_h):
    return (e-s)*(1+abs(e_h-s_h))

dp = [1] + [0]*(N-1)
def sol():
    for i in range(N-1):
        if dp[i] == 1:
            for j in range(i+1,N):
                if dp[j] == 1:
                    pass
                elif cal(i,j,lst[i],lst[j]) <= K:
                    dp[j] = 1
                    if j == N-1:
                        print("YES")
                        return
                elif lst[j] == lst[i] and cal(i,j,lst[i],lst[j]) > K:
                    break

    if dp[-1] == 0:
        print("NO")
    else:
        print("YES")

sol()

# 백준 1등

# import sys
# def input():
#     return sys.stdin.readline().rstrip()

# N, K = map(int,input().split())
# lst = list(map(int,input().split()))

# def cal(s,e,s_h,e_h):
#     return (e-s)*(1+abs(e_h-s_h))

# dp = [1] + [0]*(N-1)

# for i in range(1,N):
#     for j in range(i-1,-1,-1):
#         if dp[j] == 1 and (i-j) * (1+abs(lst[i]-lst[j])) <= K:
#             dp[i] = 1
#             break
#         if i-j > K:
#             print(i,j)
#             break
        
# print(['NO','YES'][dp[-1]])