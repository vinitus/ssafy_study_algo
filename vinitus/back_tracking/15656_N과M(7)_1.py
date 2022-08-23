import sys

n, m = map(int, sys.stdin.readline().split())

l = sys.stdin.readline().split()
l.sort(key=lambda x: int(x))

result = []

# 그냥 " 숫자"를 계속 더해주는 구조
def visit(seq, r):

    if r == 0:
        result.append(seq[1:])
        return

    for num in l:
        visit(seq + ' ' + num, r-1)

visit('', m)
print('\n'.join(result))