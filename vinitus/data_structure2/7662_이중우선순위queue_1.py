from heapq import heappush,heappop
import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(1,T+1):
    k = int(input())
    max_Q = []
    min_Q = []
    min_dict = {}
    max_dict = {}
    for idx in range(k):
        order, n = input().split()
        if order == "I":                                                    # I는 push
            heappush(max_Q, -int(n))                                  # 최대힙이기 때문에 -를 해주고 idx와 묶음
            heappush(min_Q, int(n))                                   # 최소힙. idx와 묶음
        else:
            if n == "-1":                                                   # 최소힙에서 빼기
                while True:
                    if len(min_Q) == 0:
                        break
                    pop_num = heappop(min_Q)
                    if pop_num in max_dict:
                        if max_dict[pop_num] != 0:
                            max_dict[pop_num] -= 1
                    if pop_num in min_dict:
                        min_dict[pop_num] += 1
                    else:
                        min_dict[pop_num] = 1
                    break

            else:
                while True:
                    if len(max_Q) == 0:
                        break
                    pop_num = heappop(min_Q)
                    if pop_num in min_dict:
                        if min_dict[pop_num] != 0:
                            min_dict[pop_num] -= 1
                    if pop_num in max_dict:
                        max_dict[pop_num] += 1
                    else:
                        max_dict[pop_num] = 1
                    break
    max_value = None
    min_value = None
    while True:
        if len(min_Q) == 0:
            break
        pop_num = heappop(min_Q)
        if pop_num in max_dict:
            if max_dict[pop_num] != 0:
                max_dict[pop_num] -= 1
                continue
        max_value = pop_num
        break
    while True:
        if len(max_Q) == 0:
            break
        pop_num = heappop(max_Q)
        if pop_num in min_dict:
            if min_dict[pop_num] != 0:
                min_dict[pop_num] -= 1
                continue
        min_value = pop_num
        break
    #생략