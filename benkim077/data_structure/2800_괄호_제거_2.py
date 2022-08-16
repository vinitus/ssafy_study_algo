from itertools import combinations
import sys

input = sys.stdin.readline

s = input().rstrip()

l = []
stack = []
answer = set()

for idx, v in enumerate(list(s)):
    if v == '(':
        stack.append(idx)
    elif v == ')':
        start = stack.pop()
        end = idx
        l.append([start,end])

print(l)

for i in range(1,len(l)+1):
    combi = combinations(l,i)
    for j in combi:
        tmp = list(s)
        for k in j:
            start,end = k
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))

for i in sorted(list(answer)):
    print(i)
