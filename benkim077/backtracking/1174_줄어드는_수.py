'''런타임에러(NameError)'''

import sys
sys.stdin = open('input.txt')

def dfs(k, ans):
    global decrease_number_lst

    # 가지치기
    if k > 0:
        if ans[k - 1] == ans[k] == 0:
            pass
        elif ans[k - 1] == 0 and ans[k] != 0:
            for i in range(1, k):
                if ans[i - 1] == ans[i] == 0:
                    pass
                else:
                    return
        else:
            if not (ans[k - 1] > ans[k]):
                return

    # 종료 조건
    if len(ans) == 10:
        decrease_number_lst.append(ans)
        if len(decrease_number_lst) > 1023:
            print(-1)
            sys.exit(0)
        if len(decrease_number_lst) == N:
            print(int(''.join(map(str, decrease_number_lst[N - 1]))))
            sys.exit(0)
        else:
            return

    for i in range(10):
        dfs(k + 1, ans + [i])

N = int(input())

decrease_number_lst = []

for i in range(10):
    dfs(0, [i])





'''시간초과


def solve():
    global N

    cnt = 0
    for num in range(9876543211):
        temp = num  # 계산에 사용할 임시 변수
        num_lst = []    # 줄어드는 수 판별용 리스트
        if temp == 0:
            num_lst.append(temp)
        else:
            while temp > 0:
                num_lst.append(temp % 10)
                temp //= 10
        
        for i in range(1, len(num_lst)):
            if num_lst[i] > num_lst[i - 1]:
                pass
            else:
                break
        else:
            cnt += 1
            
            if cnt == N:
                print(''.join(map(str, num_lst[::-1])))
                break
    else:
        print(-1)

N = int(input())    # N번째로 작은 줄어드는 수

solve()
'''