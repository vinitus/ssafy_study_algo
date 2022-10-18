import sys
sys.stdin = open('DP/input.txt','r')
'''
abcxyzxabc
2
abc 10
xyz 5
'''

def dfs(idx):
    # 예외처리: 범위를 벗어나면 종료
    if idx >= N:
        return 0
    
    # 이미 처리한 idx면 종료
    if dp[idx] != -1:
        return dp[idx]

    max_value = 0

    for key in dic.keys():
        
        score,len_string = dic[key][0], dic[key][1]
        
        #범위 이내라면,
        if idx + len_string-1<N:

            for check_idx in range(len_string):
                if S[check_idx+idx] != key[check_idx]:
                    break

            #존재할 경우, 해당위치에서 dfs한번더한 값과 score값을 더한 값을 maxvalue와 비교
            else:
                max_value = max(max_value,score + dfs(idx+len_string))

    # 최대값 찾는 과정
    max_value = max(max_value,1+dfs(idx+1))

    dp[idx] = max_value
    return dp[idx]

S = input()
N = len(S)

M = int(input())

# dp선언
dp = [-1] * (N+1)

dic = {}
# 딕셔너리에 점수와 문자열 길이 저장
for m in range(M):
    A, X = input().split()
    dic[A] = [int(X),len(A)]

print(dfs(0))
# print(dp)