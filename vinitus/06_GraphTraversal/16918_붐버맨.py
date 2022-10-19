import sys
def input():
    return sys.stdin.readline().rstrip()

# R, C, N = map(int,input().split())
# lst = list(list(input()) for _ in range(R))
R,C = 3,3
lst = [['O' for _ in range(3)] for _ in range(3)]
lst[1][1] = '.'
two = list(list('O' for _ in range(C)) for _ in range(R))
three = list(two[i][:] for i in range(R))
d = [(-1,0),(1,0),(0,-1),(0,1)]
for y in range(R):
    for x in range(C):
        if lst[y][x] == 'O':
            three[y][x] = '.'
            for dy,dx in d:
                if 0<= y+dy < R and 0 <= x+dx < C:
                    three[y+dy][x+dx] = '.'
four = []
for y in three:
    if 'O' in y:
        break
else:
    four = list(list('.' for _ in range(C)) for _ in range(R))

for N in range(1,12):
    if not four:
        if N % 4 == 1:
            for i in lst:
                print(''.join(i))
        elif N % 2 == 0:
            for i in two:
                print(''.join(i))
        else:
            for i in three:
                print(''.join(i))
    else:
        if N == 1:
            for i in lst:
                print(''.join(i))
        elif N % 4 == 3:
            for i in four:
                print(''.join(i))
        else:
            for i in two:
                print(''.join(i))
    print('>>>>>>>>>>>>>>>>>>>>>>>>>' + str(N))