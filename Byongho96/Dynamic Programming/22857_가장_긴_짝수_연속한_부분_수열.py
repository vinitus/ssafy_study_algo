import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

i = 0
j = 0
odds = 0
evens = 0
mx = 0
while j != N:
    if odds <= K:
        if nums[j] % 2:
            odds += 1
        else:
            evens += 1
            mx = max(mx, evens)
        j += 1
    else:
        if nums[i] % 2:
            odds -= 1
        else:
            evens -= 1
        i += 1

print(mx)