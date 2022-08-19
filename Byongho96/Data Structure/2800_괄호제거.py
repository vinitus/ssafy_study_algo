from itertools import combinations
import sys
input = sys.stdin.readline

fml = input().rstrip()

stk = []
pairLst = []
ans = set()     # 반복오류 제거!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(len(fml)):
    if fml[i] == '(':
        stk.append(i)
    elif fml[i] == ')':
        pairLst.append((stk.pop(), i))

for r in range(1, len(pairLst)+1):
    for comb in combinations(pairLst, r):
        # print(comb) # ((3, 5)) / ((0, 6)) / ((3, 5), (0,6))
        fmlLst = list(fml)
        for a, b in comb:
            fmlLst[a] = ''
            fmlLst[b] = ''
        ans.add(''.join(fmlLst))

for ans in sorted(list(ans)):
    print(ans)
