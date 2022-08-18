from heapq import heappush,heappop
import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(1,T+1):
    k = int(input())
    max_Q = []
    min_Q = []
    # index를 통해 접근하기 위한 visited
    # 왜이렇게 하냐면 힙을 두개 운용하기 때문에 하나에서 힙팝을 하면 다른 하나에서는 안됨
    # 그래서 index로 묶어주는 것이고 heap에서 [0]번째 인덱스는 항상 최소값임 -> 보이는 lst와 인덱스 구조가 다름!!!!!!
    # visited를 접근할 때 힙의 최소의 index로 접근할껀데 이렇게 접근했을 때 값이 0이라면
    # 반대편 힙에서 이미 힙팝해준거니까 힙팝을 해주면서 visited의 힙팝 idx가 1이나올때까지 계속 함
    visited = [0] * k
    for idx in range(k):
        order, n = input().split()
        if order == "I":                                                    # I는 push
            heappush(max_Q, (-int(n),idx))                                  # 최대힙이기 때문에 -를 해주고 idx와 묶음
            heappush(min_Q, (int(n),idx))                                   # 최소힙. idx와 묶음
            visited[idx] = 1                                                # visitd
        else:
            if n == "-1":                                                   # 최소힙에서 빼기
                while min_Q and not visited[min_Q[0][1]]:                   # min_Q가 존재하고 max_Q에서 힙팝안햇으면
                    heappop(min_Q)
                if min_Q:                                                   # min_Q가 존재하면
                    visited[min_Q[0][1]] = 0                                # max_Q에서도 빼줘야하니깐 visited의 idx에 표시
                    heappop(min_Q)
            else:
                while max_Q and not visited[max_Q[0][1]]:
                    heappop(max_Q)
                if max_Q:
                    visited[max_Q[0][1]] = 0
                    heappop(max_Q)

    while min_Q and not visited[min_Q[0][1]]:                               # 연산 하고도 남아잇을수도잇슴
        heappop(min_Q)
    while max_Q and not visited[max_Q[0][1]]:
        heappop(max_Q)


    if not min_Q or not max_Q:
        print("EMPTY")
    else:
        print(f'{-max_Q[0][0]} {min_Q[0][0]}')