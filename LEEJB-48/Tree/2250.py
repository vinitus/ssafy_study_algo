import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
tree = [[-1, -1] for i in range(N + 1)] #tree[node][0] left, 1 right
matrix = [[] for i in range(N + 1)]
num_sum = (N * (N + 1)) // 2
for i in range(N):
    node, left, right = map(int, input().split())
    if left >= 0:
        tree[node][0] = left
        num_sum -= left
    if right >= 0:
        tree[node][1] = right
        num_sum -= right
count = 1


def traverse(node, depth):
    global count

    left, right = tree[node]

    if left >= 0:
        traverse(left, depth + 1)

    matrix[depth - 1].append(count)

    count += 1
    if right >= 0:
        traverse(right, depth + 1)


traverse(num_sum, 1)
print(matrix)
min_level = 1
max_width = 0

for i in range(len(matrix)):
    stack = matrix[i]
    if not stack:
        break
    elif len(stack) == 1:
        continue
    else:
        width = stack[-1] - stack[0]
        if width > max_width:
            max_width = width
            min_level = i + 1

print(min_level, max_width + 1)
