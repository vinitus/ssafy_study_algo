import sys
def input():
    return sys.stdin.readline().rstrip()

num_of_choo = int(input())
choo_weight_list = list(map(int,input().split()))
_ = int(input())
marble_weight_list = list(map(int,input().split()))

# dp[i][j]에서 i는 사용된 추의 갯수를 의미하고
# j는 추의 갯수에 따른 나타낼 수 있는 무게를 뜻하고
# dp[i][j]의 값이 1인 것은 i개 갯수의 추를 사용해서 j라는 무게를 나타낼 수 있다는 것
dp = [[0 for _ in range((i+1)*500+1)] for i in range(num_of_choo+1)]
visited = []

def backtracking(idx,weight):
    if idx > num_of_choo:
        return 
    
    if dp[idx][weight]:
        return
    
    dp[idx][weight] = 1
    
    backtracking(idx+1, weight)
    backtracking(idx+1, weight+choo_weight_list[idx-1])
    backtracking(idx+1, abs(weight-choo_weight_list[idx-1]))
    
backtracking(0,0)

for i in marble_weight_list:
    if i > 30*500:
        visited.append("N")
        continue
    if dp[num_of_choo][i] == 1:
        print()
        visited.append("Y")
    else:
        visited.append("N")

print(*visited)