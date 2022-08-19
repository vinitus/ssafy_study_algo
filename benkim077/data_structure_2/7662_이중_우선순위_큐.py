'''
시간초과 어떻게 하지?
어떻게 h_mn과 h_mx를 매핑하지?


import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
input = sys.stdin.realine

T = int(input())
for _ in range(T):
    k = int(input())

    h_mn = list()
    h_mx = list()
    for _ in range(k):
        cmd, value = input().split()
        value = int(value)

        if cmd == 'I':
            heappush(h_mn, value)
            heappush(h_mx, -value)
        else:
            if h_mx and h_mn:
                if value == 1:
                    idx = -heappop(h_mx)
                    idx = h_mn.index(idx)
                    h_mn.pop(idx)
                else: 
                    idx = -heappop(h_mn)
                    idx = h_mx.index(idx)
                    h_mx.pop(idx)

    if h_mx and h_mn:
        print(f'{-heappop(h_mx)} {heappop(h_mn)}')
    else:
        print('EMPTY')
'''