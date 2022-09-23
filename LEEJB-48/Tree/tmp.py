import math
import sys


def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")

#############################

T = int(input())


def is_run(lis, card_num):
    if 2 <= card_num <= 7:
        if lis[card_num - 1]:
            if lis[card_num - 2] or lis[card_num + 1]:
                return True
        elif lis[card_num + 1]:
            if lis[card_num + 2]:
                return True
    elif card_num == 0:
        if lis[card_num + 1] and lis[card_num + 2]:
            return True
    elif card_num == 1:
        if lis[card_num + 1]:
            if lis[card_num - 1] or lis[card_num + 2]:
                return True
    elif card_num == 9:
        if lis[card_num - 1] and lis[card_num - 2]:
            return True
    else:
        if lis[card_num - 1]:
            if lis[card_num - 2] or lis[card_num + 1]:
                return True


answer = ''
for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    ans = 0
    for i in range(4):
        if i % 2 == 0:
            p1[cards[i]] += 1
        else:
            p2[cards[i]] += 1
    for i in range(4, len(cards)):
        if i % 2 == 0:
            p1[cards[i]] += 1
            if p1[cards[i]] == 3 or is_run(p1, cards[i]):
                ans = 1
                break
        else:
            p2[cards[i]] += 1
            if p2[cards[i]] == 3 or is_run(p2, cards[i]):
                ans = 2
                break
    answer += f'#{test_case} {ans}\n'
print(answer)
