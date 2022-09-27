# 76 ms
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
points = list(map(int, input().split()))

points.sort()
diff = [0] * (N - 1)
for i in range(N - 1):
    diff[i] = points[i + 1] - points[i]
diff.sort(reverse=True)

print(sum(diff[K-1:]))