import sys
sys.stdin = open('input.txt')


data = list(input())
for i in range(0, len(data) - 3):
    if data[i:i + 4] == ['X', 'X', 'X', 'X']:
        for j in range(4):
            data[i + j] = 'A'

for i in range(0, len(data) - 1):
    if data[i:i + 2] == ['X', 'X']:
        for j in range(2):
            data[i + j] = 'B'

if 'X' in data:
    ans = -1
    print(ans)
else:
    for i in range(len(data)):
        print(data[i], end='')
