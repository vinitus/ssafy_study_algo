# 2652ms
# min으로 바꾸니까 1040ms
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
boxes = [0] * M
for i in range(M):
    boxes[i] = list(map(int, input().split()))
boxes.sort(key=lambda x: (x[1], x[0]))

total_moved = 0
available = [C] * (N + 1)
for box in boxes:
    # mn = C
    # for idx in range(box[0], box[1]):
    #     mn = min(mn, available[idx])
    mn = min(available[box[0]:box[1]])
    if mn > 0:
        moved = min(mn, box[2])
        for idx in range(box[0], box[1]):
            available[idx] -= moved
        total_moved += moved

print(total_moved)