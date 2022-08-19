# 252ms
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dict = {}
lst = []
for i in range(N):
    name = input().rstrip()
    lst.append(name)
    dict[name] = i

for _ in range(M):
    tar = input().rstrip()
    if tar.isdigit():           # 입력 자료가 숫자형일 경우
        print(lst[int(tar)-1])      # 리스트에서 인덱스로 탐색
        continue
    print(dict[tar] + 1)        # 문자형일 경우, 딕셔너리에서 탐색
