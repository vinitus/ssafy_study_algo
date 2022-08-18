# Simple circular  348ms
# deque로 푸는게 더 빠름   232ms
N = int(input())

# Making the Queue
start = 0
end = N-1
circleQue = [0] * N
for i in range(1, N+1):
    circleQue[i-1] = i

for _ in range(N-1):        # 한개만 남을 때까지 반복
    start = (start + 1) % N     # pop

    end = (end + 1) % N         # 뒤로보내기
    circleQue[end] = circleQue[start]
    start = (start + 1) % N

print(circleQue[start])