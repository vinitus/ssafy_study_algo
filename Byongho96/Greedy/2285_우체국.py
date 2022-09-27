# 1480 ms
import sys
input = sys.stdin.readline

# [1]. 이진탐색
def distance(position):
    dist = 0
    for i in range(N):
        dist += abs(position-X[i]) * A[i]
    return dist

def BinarySearch(start, end):   # 이진 탐색의 변형
    while start < end:                              # 무조건 결과가 나오므로, < 를 슨다
        middle = (start + end) // 2
        if distance(middle) <= distance(middle+1):  # 같을 경우, 최솟값을 구해야 하므로, end를 왼쪽으로 옮겨준다
            end = middle
        else:
            start = middle + 1
    return start                                    # start == end가 되는 시점에 반환

N = int(input())
X = [0] * N
A = [0] * N
for i in range(N):
    X[i], A[i] = map(int, input().split())

print(BinarySearch(-1000000000, 1000000000))


