import sys
def input():
    return sys.stdin.readline().rstrip()
#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################
N = int(input())
road = list(map(int,input().split()))
city = list(map(int,input().split()))
i = 0
ans = 0
city[-1] = -1
while i<N-1:
    for index in range(i+1,N):
        if city[index] < city[i]:
            ans += sum(road[i:index])*city[i]
            i = index
            break
print(ans)

