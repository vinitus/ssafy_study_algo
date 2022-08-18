from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
##################################################
# deque 구현 92ms
# people = []
# for n in range(1, N + 1):
#     people.append(n)
# people = deque(people)
#
# lst = []
# for _ in range(N):
#     people.rotate(-(K-1)) # 죽은 사람을 건너뛰면서 카운팅 하기 위해서 while 반복문
#     lst.append(str(people.popleft()))
# print('<' + ', '.join(lst) + '>')
##################################################
# list 구현 68ms
people = []
for n in range(1, N + 1):
    people.append(n)
lst = []

i = 0
for _ in range(N):
    i = (i + K -1) % len(people)
    lst.append(str(people.pop(i)))
print('<' + ', '.join(lst) + '>')
##################################################
# while문 활용 시간 초과
# people = [1] * N
# removed = []
#
# i = -1  # 첫번째 경우의 예외 카운팅 요인 제거
# for _ in range(N):
#     cnt = 0
#     while cnt != K: # 죽은 사람을 건너뛰면서 카운팅 하기 위해서 while 반복문
#         i = (i + 1) % N
#         if people[i] == 1:
#             cnt += 1
#     people[i] = 0
#     removed.append(str(i+1))
#
# print('<' + ', '.join(removed) + '>')