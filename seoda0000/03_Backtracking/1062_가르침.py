import sys
def input():
    return sys.stdin.readline().rstrip()
def dfs(idx, cnt):  # (알파벳 인덱스, 추가로 배운 글자 수)
    global ans

    if cnt == k - 5:    # 종료조건 : 할당된 수를 다 배웠을 때
        readw = 0           # 읽을 수 있는 단어 수
        for word in words:
            for w in word:  # 읽을 수 있는지 체크
                if not learn[ord(w) - ord('a')]:
                    break
            else:
                readw += 1
        if ans < readw:     # 최대값 갱신
            ans = readw
        return
    for i in range(idx, 26):
        if not learn[i]:      # 아직 안 배운 알파벳이라면
            learn[i] = True   # 배운 후 다음 알파벳으로
            dfs(i+1, cnt+1)
            learn[i] = False  # clear


n, k = map(int, input().split())
if k < 5:      # 5보다 작으면 아무 단어도 못 읽음
    print(0)
    exit()
elif k == 26:  # 26이면 모두 읽을 수 있음
    print(n)
    exit()

ans = 0
words = [set(input()) for _ in range(n)]  # 단어마다 필요한 알파벳 집합
learn = [0]*26                            # 알파벳 리스트

for c in ('a', 'c', 'i', 'n', 't'):       # 꼭 배워야 할 알파벳
    learn[ord(c) - ord('a')] = 1          # 리스트에 기록


dfs(0, 0)

print(ans)
