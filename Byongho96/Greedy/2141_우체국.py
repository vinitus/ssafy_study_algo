import sys
input = sys.stdin.readline

# 우체국은 마을 위치에 있어야 한다.

# # [1]. 이진탐색
# def distance(position):
#     dist = 0
#     for i in range(N):
#         dist += abs(position-X[i]) * A[i]
#     return dist
#
# def BinarySearch(start, end):
#     answer = -1
#     while start <= end:  # `<=`should be used!
#         middle = (start + end) // 2
#         if distance(middle) <= distance(middle+1):
#             end = middle - 1
#             answer = middle
#         else:
#             start = middle + 1
#     return answer
#
# N = int(input())
# X = [0] * N
# A = [0] * N
# for i in range(N):
#     x, a = map(int, input().split())
#     X[i] = x
#     A[i] = a
#
# print(BinarySearch(0, N-1))


# 모든 마을은 일직선 위에 있다.
# X = [10, 20]
# A = [5, 15]

# [2]. 누적된 인구수의 합이 전체 인구의 반 이상이 되는 마을위에 있어야 한다...
    # N1   /       우체국(N2)      /   M   : distance
    # N1   /   N2   /  우체국 + 1  /   M   : distance + N1 + N2 - M
                                        # (N1 + N2 > M)이면 증가
                                        # (N1 + N2 < M)이면 감소
                                        # (N1 + N2 = M)이면 유지

N = int(input())
arr = []
people = 0
for _ in range(N):
    pos, num = map(int, input().split()) # [(마을위치, 인구)]
    arr.append((pos, num))
    people += num

arr.sort()

postoffice = -1
people_left = 0
for i in range(N):
    people_left += arr[i][1]
    if people_left >= people/2:         # //가 아니라 /
                                        # N1, N2 >= M이 지점을 찾아야함
                                        # 총 인원이 5명일 경우 3명이 되는 지점을 찾아야 함
        postoffice = arr[i][0]
        break

print(postoffice)



#####################################################
# 완전탐색
# N = int(input())
# X = [0] * N
# A = [0] * N
#
# mn = 1000000001
# mx = 0
# for i in range(N):
#     x, a = map(int, input().split())
#     X[i] = x
#     A[i] = a
#     if x < mn:
#         mn = x
#     if mx < x:
#         mx = x
#
# mn_dist = 1000000001 ** 2
# position = -1
# for pos in range(mn, mx + 1):
#     dist = 0
#     for i in range(N):
#         dist += abs(pos-X[i]) * A[i]
#     if dist < mn_dist:
#         mn_dist = dist
#         position = pos
#
# print(position)


