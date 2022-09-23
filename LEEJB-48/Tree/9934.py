import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

K = int(input())
visited = list(map(int,input().split()))
i = 0
max_num = 2**K
arr = [None] * max_num


def traverse(rt):
    global i
    left = rt*2
    right = rt*2 + 1
    if left < max_num:
        traverse(left)
    arr[rt] = visited[i]
    i += 1
    if right < max_num:
        traverse(right)
traverse(1)
ans = ""
p = 0
index = 1
while True:
    if p >= K:
        break
    for _ in range(2**p):
        ans += str(arr[index])+' '
        index += 1
    ans += '\n'
    p += 1
print(ans)

