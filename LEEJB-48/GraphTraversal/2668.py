import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

nums = [int(input()) for _ in range(N)]
ans = 0
ans_nums = set()
for i in range(N):  # i는 인덱스값
    if not nums[i]:
        continue
    if nums[i] == i + 1:
        ans += 1
        nums[i] = 0
        ans_nums.add(i + 1)
        continue
    else:
        visited = [0] * N
        index = i
        cnt = 1
        tmp_nums = []
        while True:
            if not nums[index]:
                if visited[index]:
                    tn = cnt - visited[index]
                    ans += tn
                    ans_nums.update(tmp_nums[len(tmp_nums) - tn:])
                    break
                else:
                    break
            next = nums[index] - 1
            tmp_nums.append(next + 1)
            nums[index] = 0
            visited[index] = cnt
            index = next
            cnt += 1

print(ans)
print(*sorted(list(ans_nums)), sep='\n')
