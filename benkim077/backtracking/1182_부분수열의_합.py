import sys
sys.stdin = open('input.txt')

# lst의 k 번째 값을 수열에 포함 시킬 것인지 말 것인지를 결정하는 함수
def dfs(k, lst, ans):
    global cnt

    if k == N:  # N-1번째 인덱스까지 결정하고, N까지 도달하면 종료
        if sum(ans) == S and ans:
            cnt += 1
        return

    # k번째 인덱스 값을 포함하는 경우
    dfs(k + 1, lst, ans + [lst[k]])
    # k번째 인덱스 값을 포함하지 않는 경우
    dfs(k + 1, lst, ans)

N, S = map(int, input().split())
lst = sorted(list(map(int, input().split())))
cnt = 0 # 합이 S인 수열의 갯수를 카운트

dfs(0, lst, [])  # 0번 인덱스부터 시작

print(cnt)