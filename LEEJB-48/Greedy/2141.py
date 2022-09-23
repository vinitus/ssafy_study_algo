import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

N = int(input())
arr = []
total_people = 0
for _ in range(N):
    lis = list(map(int,input().split()))
    total_people += lis[1]
    arr.append(lis)
arr.sort(key=lambda x:x[0])
target_people = round(total_people/2)
cur_sum_people = 0
for posi,people in arr:
    cur_sum_people += people
    if cur_sum_people >= target_people:
        print(posi)
        break