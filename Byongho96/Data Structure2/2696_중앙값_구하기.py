## 88ms
## 최대 힙인 mn_heap과 최소 힙인 mx_heap을 두고, num의 값을 mn_heap[0], mx_heap[0]과 비교
import heapq
import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):

    N = int(input())
    print(N // 2 + 1)

    nums = []
    for _ in range(N // 10 + 1):
        nums += list(map(int, input().rstrip().split()))

    mx_heap = []
    mn_heap = []
    moor = nums[0]
    print_lst = [moor]
    for i in range(1, N//2 + 1):
        num_even = nums[2 * i - 1]
        if num_even >= moor:
            heapq.heappush(mx_heap, num_even)
            heapq.heappush(mn_heap, -moor)
        else:
            heapq.heappush(mx_heap, moor)
            heapq.heappush(mn_heap, -num_even)

        moor = nums[2 * i]
        if moor < -mn_heap[0]:
            tmp = moor
            moor = -heapq.heappop(mn_heap)
            heapq.heappush(mn_heap, -tmp)
        elif moor > mx_heap[0]:
            tmp = moor
            moor = heapq.heappop(mx_heap)
            heapq.heappush(mx_heap, tmp)
        else:
            pass

        print_lst.append(moor)

    if N < 21:
        print(*print_lst)
    else:
        for i in range((N // 2 + 1)//10):
            print(*print_lst[i*10:(i+1)*10])
        print(*print_lst[(i+1)*10:])
