
def pibo(n):
    if n < 2:
        return n
    if memo[n]:
        return memo[n]
    memo[n] = pibo(n-1) + pibo(n-2)
    return memo[n]

n = int(input())

memo = [0] * 21
print(pibo(n))

# pibo_prev = 0
# pibo = 1
#
# if n == 0:
#     pibo = 0
# elif n == 1:
#     pibo =1
# else:
#     for _ in range(n-1):
#         pibo, pibo_prev = (pibo + pibo_prev), pibo
#
# print(pibo)

'''
#최단 코드 참조
n = int(input())

pibo_prev = 0
pibo = 1

for _ in range(n):
    pibo, pibo_prev = (pibo + pibo_prev), pibo
    
print(pibo_prev)
'''

