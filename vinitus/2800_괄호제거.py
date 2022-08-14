from itertools import combinations

s = input()

case_lst = []
stk = []
answer = set()

for idx, num in enumerate(list(s)):
    if num == '(':
        stk.append(idx)
    elif num == ')':
        start = stk.pop()
        end = idx
        case_lst.append([start,end])

for i in range(1,len(case_lst)+1):
    combi = combinations(case_lst,i)
    for j in combi:
        tmp = list(s)
        for k in j:
            start,end = k
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))


for i in sorted(list(answer)):
    print(i)