import sys
def input():
    return sys.stdin.readline().rstrip()


#######제출할 때 지우세요!!!#######
sys.stdin = open("input.txt", "r")
#############################


def backtracking(i,bits,k):
    if k == target:
        tmp_set2 = {all_letters[i] for i in range(len(all_letters)) if bits[i]}
        tmp_num = 0
        for s in all_sets:
            if not s-tmp_set2:
                tmp_num += 1
        global ans
        ans = max(tmp_num,ans)
        return None
    if i >= length:
        return None
    tmp_bits=bits[:]
    backtracking(i+1,tmp_bits[:],k)
    tmp_bits[i] = 1
    backtracking(i+1,tmp_bits[:],k+1)


N,K = map(int,input().split())
all_sets = []
all_letters = set()
antic = {'a','n','t','i','c'}
for i in range(N):
    tmp_set =  set(list(input().rstrip('tica').lstrip('anta'))) - antic
    all_sets.append(tmp_set)
    all_letters |= tmp_set

all_letters = list(all_letters)

bitmasks = [0] * len(all_letters)

if K < 5:
    print(0)
else:
    ans = 0
    length = len(all_letters)
    target = K-5
    backtracking(0,bitmasks,0)
    print(ans)