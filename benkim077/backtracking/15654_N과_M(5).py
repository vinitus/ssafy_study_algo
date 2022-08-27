import sys
sys.stdin = open('input.txt')

# k 번째 수열의 값을 선택하는 함수
# lst: 주어진 자연수 리스트
# vsted: 자연수 리스트에서 사용한 것을 체크함
# prev: 수열의 k - 1번째 값
# ans: 수열을 저장하는 리스트
def dfs(k, sorted_lst, vsted, ans): 
    # 종료 조건
    if k == M:
        print(*ans)
        return
    
    # k 번째 값 선택
    for ele in sorted_lst:
        if not vsted[ele[1]]:
            # 하부 함수 호출
            vsted[ele[1]] = True
            dfs(k + 1, sorted_lst, vsted, ans + [ele[0]])
            vsted[ele[1]] = False


N, M = map(int, input().split())
lst = [(v, i) for (i, v) in enumerate(map(int, input().split()))]   # (자연수 값, 인덱스) 형태로 저장된 리스트\
sorted_lst = sorted(lst)    # 오름차순 정렬

vsted = [False] * N

dfs(0, sorted_lst, vsted, [])