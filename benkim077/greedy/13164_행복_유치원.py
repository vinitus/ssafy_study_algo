import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
data = list(map(int, input().split()))
# [1, 3, 5, 6, 10]

if K == 1:
    print(data[-1] - data[0])
    exit()

diff_lst = [data[i] - data[i - 1] for i in range(1, N)]
# [2, 2, 1, 4]
diff_lst = list(enumerate(diff_lst))
diff_lst.sort(key=lambda x:x[1], reverse=True)

diff_lst = diff_lst[0: K - 1]

diff_lst.sort()
# print(diff_lst)
ans = 0
for i in range(len(diff_lst)):
    if i == 0:
        temp = data[:diff_lst[i][0] + 1]
        ans += max(temp) - min(temp)
        # print(temp)
    elif i == len(diff_lst) - 1:
        temp = data[diff_lst[i - 1][0] + 1:diff_lst[i][0] + 1]
        ans += max(temp) - min(temp)
        # print(temp)
        temp = data[diff_lst[i][0] + 1:]
        ans += max(temp) - min(temp)
        # print(temp)
    else:
        temp = data[diff_lst[i - 1][0] + 1:diff_lst[i][0] + 1]
        ans += max(temp) - min(temp)
        # print(temp)
    

print(ans)