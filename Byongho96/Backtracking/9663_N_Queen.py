## Pypy 30320
N = int(input())

def isPromising(i, j):
    for ii in range(i):
        if row[ii] == j or abs(row[ii] - j) == i - ii:
            return False
    return True

def nQueen(i):
    global ans
    # 종료조건
    if i == N:
        # print(row)
        ans += 1
        return
    # 가지치기
    # 후고분 출력
    else:
        for j in range(N):
            row[i] = j
            if isPromising(i, j):
                nQueen(i + 1)


ans = 0
row = [0] * N
nQueen(0)
print(ans)