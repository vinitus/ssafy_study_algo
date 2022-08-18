import sys
input = sys.stdin.readline

dct = {}
lst = []
total_length = 0
while True:
    a = input().rstrip()
    if not a:
        break
    total_length += 1
    if dct.get(a):
        dct[a] += 1
    else:
        dct[a] = 1
        lst.append(a)
lst.sort()
for i in lst:
    print(f"{i} {dct[i]/total_length*100:.04f}")