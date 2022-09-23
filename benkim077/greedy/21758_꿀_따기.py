import sys
sys.stdin = open('input.txt')
N = int(input())
data = list(map(int, input().split()))

sm = sum(data) 

# 1
mx = 0
b1 = data[0]
for i in range(1, N):
    b2 = data[i]
    rlt1 = sm - b1 - b2 
    rlt2 = sum(data[i + 1:])
    mx = max(mx, rlt1 + rlt2)

# 2
b1 = data[-1]
for i in range(0, N - 1):
    b2 = data[i]
    rlt1 = sm - b1 - b2
    rlt2 = sum(data[:i])
    mx = max(mx, rlt1 + rlt2)

# 3
b1 = data[0]
b2 = data[-1]
for i in range(1, N - 1):
    b_home = data[i]
    rlt1 = sum(data[1:i + 1])
    rlt2 = sum(data[i:-1])
    mx = max(mx, rlt1 + rlt2)

print(mx)