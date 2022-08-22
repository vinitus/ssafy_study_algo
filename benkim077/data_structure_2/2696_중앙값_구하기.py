# 데이터가 지속적으로 입출력되는 list에서 어떻게 중앙값을 구할 수 있을까?
# 기존 중앙값을 기준으로
    # 작은 값은 max_heap에 넣고
    # 큰 값은 min_heap에 넣는다.
# 새로운 중앙값을 구하려면, len(max_heap)과 len(min_heap)이 같아져야 한다.
# 그러므로 두 힙 중에 길이가 더 긴 힙에서 heappop연산을 하면 새로운 중앙값을 구할 수 있다.


import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())

    # 입력값 format 변환
    input_times = (M // 10) + 1                                 # 입력값 받는 횟수
    data = [0]                                                  # data를 저장할 1차원 리스트 (반복문에서 i 맞춰주려고 0 넣음)
    temp = list(input().split() for _ in range(input_times))    # 2차원 배열을 1차원 배열로 변경할 때 사용하는 임시 리스트
    for i in range(input_times):                                # 2차원 배열 > 1차원 배열로 변경
        for j in range(len(temp[i])):
            data.append(int(temp[i][j]))

    minH, maxH = [], []                 # 최소 힙, 최대 힙
    med = data[1]                       # 초깃값
    ans = [med]                         # 중앙값들이 저장되는 리스트
    for i in range(2, M + 1):           # 2번째부터 M번째까지
        # 값 분류 및 heappush
        if data[i] >= med:                  # med 보다 크거나 같으면 최소 힙으로
            heappush(minH, data[i])
        else:                               # med 보다 작으면 최대 힙으로
            heappush(maxH, -data[i])

        # 새로운 중앙값 구하기(홀수 번째 마다)
        if i % 2 == 1:
            if len(minH) > len(maxH):       # 최소 힙이 더 긴 경우
                heappush(maxH, -med)
                med = heappop(minH)
            elif len(minH) == len(maxH):    # 길이가 같은 경우
                pass
            else:                           # 최대 힙이 더 긴 경우
                heappush(minH, med)
                med = -heappop(maxH)
            ans.append(med)                 # 새로운 중앙값 ans에 넣기

    # 출력
    print(len(ans))
    num = (len(ans) // 10) + 1
    for i in range(num): 
        temp = ans[10 * i:10 * (i + 1)]     # i == 0 일 때, ans[0:10]. i == 1일 때, ans[10:20]
        print(' '.join(map(str, temp)))
