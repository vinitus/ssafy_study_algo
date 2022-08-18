import sys
from heapq import heappop as hpop, heappush as hpush
from collections import defaultdict

input = sys.stdin.readline


def solution(input):
    for _ in range(int(input())):
        minQ = []
        maxQ = []
        counter = defaultdict(int)
        length = 0
        for _ in range(int(input())):
            command, i = input().split()
            match command:
                case "I":
            i = int(i)
            hpush(minQ, i)
            hpush(maxQ, -i)
            length += 1
            counter[i] += 1
        case
        "D":
        if length:
            match i:
            case
            "1":
            while maxQ and counter[d := -hpop(maxQ)] == 0: pass
        case
        "-1":
        while minQ and counter[d := hpop(minQ)] == 0: pass


counter[d] -= 1
length -= 1
if length == 0:
    minQ.clear()
    maxQ.clear()
    counter.clear()

if sum(counter.values()):
    while maxQ and counter[M := -hpop(maxQ)] == 0: pass
    while minQ and counter[m := hpop(minQ)] == 0: pass
    print("%d %d" % (M, m))
else:
    print("EMPTY")

solution(input)