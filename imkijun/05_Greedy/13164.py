import sys
sys.stdin = open("Greedy/input.txt","r")

N, K = map(int, input().split())

li = list(map(int, input().split()))

dif = []

for i in range(1,N):
    dif.append(li[i]-li[i-1])

dif.sort(reverse=True)

print(sum(dif[K-1:]))

'''
풀이방법
1. 3조로 나눈다고 하면, 칸막이 (3-1)개를 집어넣어 구별 가능

2. dif 리스트에 밀접해 있는 원생의 키 차이를 삽입
2-1. 헷갈려서 예시에 하나 더 추가해봄 li.append(15)
# li =[1,3,5,6,10,15], dif = [2,2,1,4,5]

3. 숫자 차이가 큰 4,5가 방을 따로 써야 될것만 같은 느낌

4. dif.sort(reverse= True) -> dif = [5,4,2,1,1], sum(dif[K-1:])

'''