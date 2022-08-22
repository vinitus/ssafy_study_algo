from heapq import heappush,heappop
import sys
def input():
    return sys.stdin.readline().rstrip()

def dayCal(M,d):
    while True:
        M -= 1
        if M == 0:
            return d
        elif M % 2 == 1:
            if M <= 7:
                d += 31
            else:
                d += 30
        else:
            if M == 2:
                d += 28
            else:
                if M <= 6:
                    d += 30
                else:
                    d += 31

def minuteCal(d,h,m):
    return d * 24 * 60 + h * 60 + m

N, L, F = input().split()
N, F = int(N), int(F)
D = int(L.split("/")[0])
H,M = map(int,L.split("/")[1].split(":"))
M = minuteCal(D,H,M)

dct = {}
answer = {}

for _ in range(N):
    lst = input()
    _, month, day = map(int,lst.split()[0].split("-"))
    day = dayCal(month, day)
    hour, minute = map(int,lst.split()[1].split(":"))
    minute = minuteCal(day,hour,minute)
    what = lst.split()[2]
    who = lst.split()[3]
    if what not in dct:
        dct[what] = [who, minute]
    else:
        tmp = minute - dct[what][1]
        if M >= tmp:
            continue
        else:
            if who not in answer:
                answer[who] = (tmp-M) * F
            else:
                answer[who] += (tmp-M) * F
        del dct[what]

if answer:
    for key,value in sorted(answer.items()):
        print(key,value)
else:
    print(-1)