for _ in range(int(input())):

    N, M = map(int, input().split())

    printQue = list(map(int, input().split()))
    cnt = 0
    mxIdx = 0
    mx = printQue[0]
    for _ in range(N):
        for i in range(mxIdx, mxIdx + N):   # 다음 최댓값을, 최댓값 다음 인덱스부터 구하기
            i %= N
            if printQue[i] > mx:
                mxIdx = i
                mx = printQue[mxIdx]
        printQue[mxIdx] = 0 # 해당 요소 프린트 하기
        cnt += 1
        mx = 0
        if mxIdx == M:
            print(cnt)
            break