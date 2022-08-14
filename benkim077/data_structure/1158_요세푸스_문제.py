N, K = map(int, input().split())

lst = list(range(1, N+1))
ans = []

idx = 0
while lst:
    idx = (idx + K - 1) % len(lst)
    ans.append(lst.pop(idx))

print(f'<{str(ans)[1:-1]}>')



# N, K = map(int, input().split())

# lst = [i for i in range(1, N+1)]

# cnt, idx = 0, 0
# ans = []

# while len(lst) > 0:
#     cnt += 1
#     if cnt % K == 0:
#         ans.append(lst.pop(idx))
#     else:
#         idx += 1

#     if len(lst) == 0:
#         pass
#     elif idx == len(lst):
#         idx = idx % len(lst)

# print(f'<{str(ans)[1:-1]}>')
