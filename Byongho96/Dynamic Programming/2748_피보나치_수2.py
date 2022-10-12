N = int(input())

if N == 0:
    pibo = 0
elif N == 1:
    pibo = 1
else:
    pibo = 1
    pre_pibo = 0
    for _ in range(N-1):
        pibo, pre_pibo = (pibo + pre_pibo), pibo

print(pibo)