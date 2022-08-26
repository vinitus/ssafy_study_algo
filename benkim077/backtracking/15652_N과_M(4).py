import sys
sys. stdin = open('input.txt')

def dfs(k, lst, prev, ans):
    if k == M:
        print(*ans)
        return
    
    for num in lst:
        if num >= prev:
            dfs(k + 1, lst, num, ans + [num])

N, M = map(int, input().split())

lst = [i + 1 for i in range(N)] # 1 ~ N 숫자

dfs(0, lst, 0, [])
# 수열의 k번째 값을 결정하는 함수
# lst: 숫자 리스트
# prev: 수열의 k - 1 번째 값
# ans: 수열을 저장하는 곳