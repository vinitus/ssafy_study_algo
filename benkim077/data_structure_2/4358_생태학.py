'''
- 입력 갯수가 주어지지 않은 경우

- set, dict가 비슷한 면이 있다. (중복 제거)
'''
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

data = dict()
cnt = 0
while True:
    strg = input().rstrip()
    if strg:
        if data.get(strg) == None:
            data[strg] = 1
        else:
            data[strg] += 1
        cnt += 1
    else:
        break

key_lst = list(data.keys())
key_lst.sort()

for i in range(len(key_lst)):
    print(f'{key_lst[i]} {data[key_lst[i]] / cnt * 100:.4f}')


'''시간초과
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

data = []
while True:
    strg = input().rstrip()
    if strg:
        data.append(strg)
    else:
        break

# 중복 제거, 사전순 정렬
sett = list(set(data))
sett.sort()

# count
cnt_lst = [0] * len(sett)
for i in range(len(sett)):
    cnt_lst[i] = data.count(sett[i])

# 출력
for i in range(len(sett)):
    print(f'{sett[i]} {cnt_lst[i] / len(data) * 100:.4f}')
'''
