import sys
sys.stdin = open('input.txt')


def dfs(k, lst, vsted, ans):
    if k == M:
        print(ans)
        return

    temp = []
    for i in range(len(lst)):
        if not vsted[lst[i][1]]:    # 방문하지 않은 것들을 
            temp.append(lst[i])     # temp에 모은다.
    # temp에 모은 것 중 최솟값을 수열의 k번째 값으로 선택하고
    # k + 1번째 함수 호출
    num = min(temp)
    vsted[num[1]] = True
    print(vsted)
    dfs(k + 1, lst, vsted, ans + [num])
    # 리턴 받은 이후에도 계속 돌아야하는데, 그렇게 안되고 있네

N, M = map(int, input().split())
lst = [(v, i) for (i, v) in enumerate(map(int, input().split()))]
# [(4, 0), (5, 1), (2, 2)]
vsted = [False] * N

dfs(0, lst, vsted, [])