import sys


input = sys.stdin.readline

n = int(input())
stack = []
lst = []
lst_copy = lst[:]
goal_lst = []
stop_flag = False
for _ in range(n):
    lst.append(int(input()))

for i in range(n-1):
    if lst[i] + 1 == lst[i+1]:
        print("NO")
        stop_flag = True
        break

if stop_flag is not True:
    while len(goal_lst) == n:
        for i in range(n):
            for j in range(i,n):
                stack.append(lst.pop(lst.index(j)))
