import sys
sys.stdin = open('input.txt')


def dfs(k, lst, vsted, prev, ans):
    if k == M:
        print(' '.join(map(str, ans)))
        return

    for i in lst:                   # 1 ~ N 숫자 중에서 하나를 선택
        if not vsted[i] and i > prev:   # 방문하지 않고, 수열의 k-1 번째 값 보다 커야함.
            vsted[i] = True
            dfs(k + 1, lst, vsted, i, ans + [i])
            vsted[i] = False


N, M = map(int, input().split())

lst = [i + 1 for i in range(N)]
vsted = [False] * (N + 1)

dfs(0, lst, vsted, 0, [])   
# 수열의 k번째 수를 선택하는 함수
# lst: 숫자 목록
# vsted: 방문 체커
# prev: 이전에 고른 값
# ans: 수열을 저장
