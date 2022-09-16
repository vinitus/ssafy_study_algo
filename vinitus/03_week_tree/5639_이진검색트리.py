import sys
sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().rstrip()

lst = []
a = input()

while a != "":
    lst.append(int(a))
    a = input()

N = len(lst)

def sol(s,e):
    if s > e:           # 종료 조건
        return
    mid = e + 1         #
    for i in range(s+1,e+1):        # 기준점 s부터 e + 1(최대 N-1)까지
        if lst[s] < lst[i]:         # 오른쪽이 더 크다 -> 현재 s 기준 오른쪽으로 갈 분기점임
            mid = i
            break
    sol(s+1, mid - 1)
    sol(mid, e)
    print(lst[s])

sol(0,N-1)