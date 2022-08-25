import sys
sys.stdin = open('input.txt')

def dfs(k, lst, vsted, ans):
    if k == M:
        print(ans)
        return

    for i in range(1, N + 1):
        if not vsted[i]:
            vsted[i] = True
            dfs(k + 1, lst, vsted, ans + [k])
            vsted[i] = False


N, M = map(int, input().split())

lst = [i + 1 for i in range(N)] # 1 부터 N 이 들어있는 리스트
vsted = [False] * (N + 1)

dfs(0, lst, vsted, [])   # 0번째 상태 공간 트리부터, 길이 0 부터