# 각 센서의 좌표(정수)
# 집중국의 수신 가능영역 거리의 합의 최솟값

import sys
sys.stdin = open('input.txt')


def solve():
    global K
    if len(data) == 1:
        ans = 0
        return ans
    
    # [1, 3, 6, 7, 9]
    # [1, 3 // 6, 7, 9] => 2 + 3 = 5

    # [3, 6, 7, 8, 10, 12, 14, 15, 18, 20]
    # [3 // 6, 7, 8, 10 // 12 // 14, 15 // 18, 20] => 0 + 2 + 2 + 1 + 2 = 7
    diff_lst = [0] * (len(data) - 1)
    for i in range(1, len(data)):
        diff_lst[i - 1] = data[i] - data[i - 1]
        # [2, 3, 1, 2]
        
    diff_lst = sorted(list(enumerate(diff_lst)), key=lambda x:x[1], reverse=True)
    # [(1, 3), (0, 2), (3, 2), (2, 1)]
    sm = 0
    i = 0
    while K > 1:
        sm += data[diff_lst[i][0] + 1] - data[diff_lst[i][0]]
        K -= 1
        i += 1

    ans = data[-1] - data[0] - sm
    return ans

N = int(input())
K = int(input())
data = sorted(list(set(map(int, input().split()))))

ans = solve()
print(ans)