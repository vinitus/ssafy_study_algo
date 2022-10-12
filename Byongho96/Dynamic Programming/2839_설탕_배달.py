bag = [-1] * 5001
bag[3] = 1
bag[4] = -1
bag[5] = 1
bag[6] = 2
bag[7] = -1
bag[8] = 2
bag[9] = 3
bag[10] = 2
bag[11] = 3
bag[12] = 4


N = int(input())
if N < 13:
    print(bag[N])
else:
    for i in range(13, N+1):
        bag[i] = 1 + min(bag[i - 3], bag[i - 5])
    print(bag[N])
