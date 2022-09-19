# 발표 준비

'''
1. 작은 것 부터 합친다.
2. 

40 30 30 50
40 60 50 => 60(30 + 30)
60 90 => 90(40 + 50)
150 => 150(30 + 30 + 40 + 50)
'''
import sys
sys.stdin = open('input.txt')


def solve(lst, n):
    global ans

    if n == 1:
        return


    



    # if n % 2 == 0:
    #     temp = [0] * (n // 2)
    #     for i in range(n // 2):
    #         temp[i] = lst[i * 2] + lst[i * 2 + 1]
    #         ans += temp[i]
    #     # print(temp, ans)
    #     solve(temp, n // 2)
    # else:
        # # [4, 3, 4, 4, 5, 5, 5, 14, 17, 21, 21, 32, 35, 98]
        # lst.sort()
        # temp = [0] * (n - 1)
        # temp[0] = lst[0] + lst[1]
        # ans += temp[0]
        # for i in range(1, n - 1):
        #     temp[i] = lst[i + 1]
        # solve(temp, n - 1)

        # temp = [0] * (n // 2 + 1)
        # for i in range(n // 2):
        #     temp[i] = lst[i * 2] + lst[i * 2 + 1]
        #     print(lst[i * 2], lst[i * 2 + 1])
        #     ans += temp[i]
        # i += 1
        # print(lst[i * 2])
        # temp[i] = lst[i * 2]
        # print(temp, ans)
        # solve(temp, n // 2 + 1)


T = int(input())
for _ in range(T):
    K = int(input())
    data = list(map(int, input().split()))
    
    ans = 0
    # print(data, sum(data))
    # [1, 3, 3, 4, 4, 5, 5, 5, 14, 17, 21, 21, 32, 35, 98]
    solve(data, K)

    print(ans)


