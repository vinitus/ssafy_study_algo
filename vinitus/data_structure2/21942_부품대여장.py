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

N, L, F = input().split()
N, F = int(N), int(F)
D = int(L.split("/")[0])
H,M = map(int,L.split("/")[1].split(":"))
M = H * 60 + M
dct = {}
answer = {}
for _ in range(N):
    lst = input()
    _, month, day = map(int,lst.split()[0].split("-"))
    day = dayCal(month, day)
    hour, minute = map(int,lst.split()[1].split(":"))
    minute = hour * 60 + minute
    what = lst.split()[2]
    who = lst.split()[3]
    if what not in dct:
        dct[what] = [who, day, minute]
    else:
        tmp_D = day - dct[what][1]
        tmp_M = minute - dct[what][2]
        if D > tmp_D:
            continue
        elif D == tmp_D:
            if M >= tmp_M:
                continue
            else:
                if who in answer:
                    answer[who] += F*abs(tmp_M - M)    
                else:
                    answer[who] = F*abs(tmp_M - M)
        else:
            cal_D = tmp_D - D
            cal_M = cal_D * 24 * 60 + tmp_M - M
            if who in answer:
                answer[who] += F*cal_M
            else:
                answer[who] = F*cal_M
        del dct[what]

if not answer:
    print(-1)
else:
    for key, value in sorted(answer.items()):
        print(key, value)