import sys
sys.stdin = open('input.txt')


N = int(input())

lst = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    if a > b:
        lst.append((b, a))
    else:
        lst.append((a, b))

lst = sorted(lst)

