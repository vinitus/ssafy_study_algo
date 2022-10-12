N = int(input())
nums = list(map(int, input().split()))

sm = nums[:]
mx = nums[0]
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            sm[i] = max(sm[i], sm[j] + nums[i])
            mx = max(mx, sm[i])

print(mx)