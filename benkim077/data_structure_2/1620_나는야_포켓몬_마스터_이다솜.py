'''
dct를 뒤집어서 v -> k 에 접근할 수 있게 만들었다.
다만 v가 중복되는 경우는 사용할 수 없다.
'''

N, M = map(int, input().split())

data_dct = dict()
for i in range(1, N + 1):
    data_dct[i] = input()

rev_dct = {v: k for k, v in data_dct.items()}

lst = list(input() for i in range(M))
for i in range(M):
    if lst[i].isnumeric():
        print(data_dct[int(lst[i])])
    else:
        print(rev_dct[lst[i]])
