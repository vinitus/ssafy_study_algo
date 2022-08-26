# 448ms

from collections import defaultdict
import sys
input = sys.stdin.readline

month = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
rental_dic = {}
fine_dic = defaultdict(int)

def minute_trans(D, H, m, M = 0):
    D += month[M]
    H += D * 24
    m += H * 60
    return m

N, L, F = input().rstrip().split()
N = int(N)
D_lm = int(L[:3])
H_lm = int(L[4:6])
m_lm = int(L[7:])
F = int(F)
duration_lm = minute_trans(D_lm, H_lm, m_lm)

for _ in range(N):
    YMD, HM, equip, name = input().rstrip().split()
    M_e = int(YMD[5:7])
    D_e = int(YMD[8:])
    H_e, m_e = map(int, HM.split(':'))
    time_e = minute_trans(D_e, H_e, m_e, M_e)

    if not rental_dic.get((equip, name)):
        rental_dic[(equip, name)] = time_e
    else:
        time_s = rental_dic.pop((equip, name))      # pop해서 기록을 없애줘야 함!!!!!!!!!!!!!!!!!!!
        duration = time_e - time_s
        if duration >= duration_lm + 1:
            fine = (duration - duration_lm) * F
            fine_dic[name] += fine

if fine_dic:
    fine_lst = sorted(list(fine_dic.items()))
    for ele in fine_lst:
        print(*ele)
else:
    print(-1)

