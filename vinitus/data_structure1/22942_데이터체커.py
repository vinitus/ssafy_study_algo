import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    x,r = map(int,input().split())
    front,end = x-r,x+r
    arr.append([front,i,0])
    arr.append([end,i,1])

arr.sort()
stk = []
for i in range(len(arr)):
    if arr[i][2] == 0:
        stk.append(arr[i])
    else:
        if stk[-1][2] == 0:
            if stk[-1][1] == arr[i][1]:
                stk.pop()
            else:
                print("NO")
                break
else:
    print("YES")