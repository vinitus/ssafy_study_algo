# 2개의 그룹이 있다고 생각
# 각 그룹에서 최솟값을 최대화 할 수 있도록 그룹을 뽑는 방법에 대해서.
    # 멤버 수가 3의 배수라면, 내림차순으로 정렬해서 처리
    # 멤버 수가 3의 배수가 아니라면, 
        # 3k + 1인 경우, 위의 방법과 같은 방법이 최선
        # 3k + 2인 경우, 역시 같은 방법이 최선

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
data = [0] * N
for n in range(N):
    data[n] = int(input())
data.sort(reverse=True)

total = sum(data)
minus_lst = [0] * (N//3)
k = 2
while k < N: 
    minus_lst[k//3] = data[k]
    k += 3

minus = sum(minus_lst)

print(total - minus)