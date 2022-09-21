import re
from itertools import combinations
import sys
input = sys.stdin.readline

# combinations 와 비트마스킹 활용
N, K = map(int, input().split())

if K < 5:
    print(0)
    sys.exit()

elif K >= 26:
    print(N)
    sys.exit()

# 각 단어를 비트마스킹하여, 그 값을 words에 append
words = []
for _ in range(N):
    word_bit = 0
    word = re.sub('[antic]', '', input().rstrip())
    for c in word:
        word_bit = word_bit | (1 << (ord(c) - 97))
    words.append(word_bit)

mx = 0
alphabets = tuple(map(lambda x: 2**x, (1,3,4,5,6,7,9,10,11,12,14,15,16,17,18,20,21,22,23,24,25)))
for comb in combinations(alphabets, K-5):
    comb_bit = sum(comb)
    cnt = 0
    for word in words:
        if word & comb_bit == word:
            cnt += 1
    mx = max(mx, cnt)

print(mx)

##########################################################

# 시간초과
# def backtracking(n, curIdx):
#     global mx
#     # 종료조건
#     if n == K - 5:
#         tmp = 0
#         for word in words:
#             for w in word:
#                 if not alpha[ord(w) - 97]:
#                     break
#             else:
#                 tmp += 1
#         if tmp > mx:
#             mx = tmp
#         return
#     # 후보군 출력
#     else:
#         for i in (1,3,4,5,6,7,9,10,11,12,14,15,16,17,18,20,21,22,23,24,25):
#             if not alpha[i]:
#                 alpha[i] = 1
#                 backtracking(n+1, i)
#                 alpha[i] = 0
#         return
#
# N, K = map(int, input().rstrip().split())
#
# if K < 5:
#     print(0)
#
# elif K >= 26:
#     print(N)
#
# else:
#     words = []
#     for _ in range(N):
#         word = input().rstrip()
#         words.append(set(re.sub('[antic]','',word)))
#
#     mx = 0
#     alpha = [0] * 26
#     backtracking(0, 0)
#
#     print(mx)
