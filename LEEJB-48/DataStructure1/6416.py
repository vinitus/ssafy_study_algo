import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################

while True:
    lis = []
    while True:
        tmp = input().split("  ")
        tmp_break = False
        for nums in tmp:
            if not nums:
                tmp_break = True
                break
            if nums == '0 0':
                tmp_break = True
                break
            elif nums == '-1 -1':
                exit()
            else:
                lis.append(nums)
        if tmp_break:
            break
    if not lis:
        continue
    #### 여기서부터 하자
    print(lis)