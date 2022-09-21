import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################



ans = ''
cnt = 0
board = input()
for w in board:
    if w == 'X':
       cnt += 1
    else:
        if cnt:
            if cnt%2 != 0:
                print(-1)
                exit()
            else:
                while cnt:
                    if cnt >= 4:
                        ans += 'AAAA'
                        cnt -= 4
                        continue
                    ans += 'BB'
                    cnt -= 2
        ans += '.'
if cnt:
    if cnt % 2 != 0:
        print(-1)
        exit()
    else:
        while cnt:
            if cnt >= 4:
                ans += 'AAAA'
                cnt -= 4
                continue
            ans += 'BB'
            cnt -= 2
print(ans)