from collections import deque


A, B = map(int, input().split())

# A에서 시작해서 도달 가능한 수와 횟수를 dict로 정리
greedy = {}
greedy[A] = 1

# A에서 만들 수 있는 수들의 집합 => lst
lst = deque([A*2 , A*10 +1])
cnt = 1

while lst:
    cnt += 1

    # lst의 작은 원소부터 확인
    for _ in range(len(lst)):
        l = lst.popleft()
        
        # 만들어진 숫자가 처음 등장했고, 목표 숫자보다 작으면 greedy에 숫자:횟수로 데이터 추가, lst에 해당 숫자로 만들 수 있는 수 추가
        if not greedy.get(l) and l <= B:
            greedy[l] = cnt
            lst += [l*2, l*10 +1]

# greedy 딕셔너리에 B가 존재하면 해당 횟수 print
if greedy.get(B):
    print(greedy[B])
# 없으면 -1 print
else:
    print(-1)


##################################################################

a, b = map(int, input().split())

cnt = 0
p = True
while b>a:
    temp = b
    if str(b)[-1] == '1':
        b = int(str(b)[:len(str(b))-1])
    elif b % 2 == 0:
        b //= 2
    cnt += 1
    if a == b:
        break
    
    elif b < a or temp == b:
        p = False
        break

if p:
    print(cnt+1)
else:
    print(-1)